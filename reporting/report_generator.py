'''
Created on Oct 16, 2018

@author: agagaleza
'''
from datetime import datetime
from xml.sax import saxutils
import os
import errno
from reporting.report_constants import ReportConstants

class ReportGenerator(object):
    __version__ = "0.1"
    '''
    classdocs
    '''
    


    def __init__(self,stream):
        self.title = ReportConstants.DEFAULT_TITLE
        self.description = ReportConstants.DEFAULT_DESCRIPTION
        self.stream = stream

    def get_attributes(self, json_data):
        start_time = datetime.utcnow()
        duration = 0
        try:
            start_time = json_data[-1]['Scenario_' + str(len(json_data) - 1)]["start"]
            end_time = int(json_data[0]["Scenario_0"]["stop"])
            duration = end_time - start_time
            print (end_time)
            status = []
            passed = 0
            failure = 0
            error = 0
            for x in json_data:
                for scenario in x:
                    result = ReportConstants.STATUS[x[scenario]["status"]]
                    if result == "passed":
                        passed = passed +1
                    elif result == "failed":
                        failure = failure +1
                    else:
                        error = error +1
            status.append('Pass %s'    % passed)
            status.append('Failure %s'    % failure)
            status.append('Error %s'    % error)

            if status:
                status = ' '.join(status)
            else:
                status = 'none'
        except KeyError:
            print("empty results")
        except IndexError:
            print("empty results")
        return [
            ('Start Time', self.format_unix_timestamp(start_time / 1000, '%Y-%m-%dT%H:%M:%SZ')),
            ('Duration', str(self.convert_miliseconds(duration))),
            ('Status', status),
        ]

    def generateReport(self, result):
        report_attrs = self.get_attributes(result)
        generator = 'ReportGenerator %s' % ReportGenerator.__version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        output = ReportConstants.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator = generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            ending=ending,
        )
        self.stream.write(output.encode('utf8'))
        
    def _generate_stylesheet(self):
        return ReportConstants.STYLESHEET_TMPL
    
    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            line = ReportConstants.HEADING_ATTRIBUTE_TMPL % dict(
                    name=saxutils.escape(name),
                    value=saxutils.escape(value),
                )
            a_lines.append(line)
        heading = ReportConstants.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            description=saxutils.escape(self.description),
        )
        return heading
    
    def _generate_report(self, json_data):
        
        rows = []
        scenario_id = 0
        total_passed = 0
        total_failed = 0
        total_error = 0
        for scenario in json_data:
            np = nf = ne = 0
            print (scenario)
            for step in scenario['Scenario_' + str(scenario_id)]['steps']:
                if step['status'] == "passed": np += 1
                elif step['status'] == "failed": nf += 1
                else: ne += 1
        

            row = ReportConstants.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                desc=scenario['Scenario_' + str(scenario_id)]['name'],
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (scenario_id + 1),
            )
            rows.append(row)
            step_id = 1
            for step in scenario['Scenario_' + str(scenario_id)]['steps']:
                self._generate_report_test(rows, scenario_id,step, step_id, step_id)
                step_id +=1
            scenario_id +=  1
            total_passed +=np
            total_failed += nf
            total_error += ne
        report = ReportConstants.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(total_passed + total_failed + total_error),
            Pass=str(total_passed),
            fail=str(total_failed),
            error=str(total_error),
            )
          
        return report

    def _generate_report_test(self, rows, cid,step, tid, name):
        status = ReportConstants.STATUS[step["status"]]
        has_output = bool(status != 'passed')
        tid = status + ' t%s.%s' % (cid+1,tid)
        doc = step["name"]
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and ReportConstants.REPORT_TEST_WITH_OUTPUT_TMPL or ReportConstants.REPORT_TEST_NO_OUTPUT_TMPL

        # o and e should be byte string because they are collected from stdout and stderr?
#         if isinstance(o,str):
#             # TODO: some problem with 'string_escape': it escape \n and mess up formating
#             # uo = unicode(o.encode('string_escape'))
#             uo = o.decode('latin-1')
#         else:
#             uo = o
#         if isinstance(e,str):
#             # TODO: some problem with 'string_escape': it escape \n and mess up formating
#             # ue = unicode(e.encode('string_escape'))
#             ue = e.decode('latin-1')
#         else:
#             ue = e
        uo = ''
        ue = ''
        try:
            uo = step['statusDetails']['message']
            print(uo)
            ue = step['statusDetails']['trace']
            print(ue)
        except KeyError:
            print "no error" 

        script = ReportConstants.REPORT_TEST_OUTPUT_TMPL % dict(
            id = tid,
            output = saxutils.escape(uo+ue),
        )
        class_str = 'none'
        if status == "passed":
            class_str = 'hiddenRow'
            
        style_str = 'none'
        if status == 'failed':
            style_str = 'failCase'
        elif status != 'passed':
            style_str = 'errorCase'
        else:
            style_str = 'passCase'
        row = tmpl % dict(
            tid = tid,
            Class = class_str,
            style = style_str,
            desc = desc,
            script = script,
            status = status,
        )
        rows.append(row)
        if not has_output:
            return
        
    def _generate_ending(self):
        return ReportConstants.ENDING_TMPL

    def format_unix_timestamp(self, unixtime, formatstr):
        return str(datetime.utcfromtimestamp(unixtime).strftime(formatstr))   


    def convert_miliseconds(self, ms):
        s=ms/1000
        m,s=divmod(s,60)
        h,m=divmod(m,60)
        d,h=divmod(h,24)
        s=10
        return "%d days %02d:%02d:%02d" % (d,h,m,s) 
    
json = [  
   {  
      "Scenario_0":{  
         "name":"Add new pet using POST request -- @1.1 Pets",
         "status":"broken",
         "statusDetails":{  
            "message":"KeyError: 'status'\n",
            "trace":"  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/model.py\", line 1329, in run\n    match.run(runner.context)\n  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/matchers.py\", line 98, in run\n    self.func(context, *args, **kwargs)\n  File \"features/steps/steps_pet.py\", line 69, in step_impl\n    assert_that(added_pet_json['status'], equal_to(context.pet.get_pet_status()))\n"
         },
         "steps":[  
            {  
               "name":"Given Swagger PetStore web application url is set as \"https://petstore.swagger.io/v2/\"",
               "status":"passed",
               "start":1540494392353,
               "stop":1540494392354
            },
            {  
               "name":"Given \"POST\" api pet request endpoint is set as \"pet\"",
               "status":"passed",
               "start":1540494392354,
               "stop":1540494392355
            },
            {  
               "name":"When HEADER params for request and response are specified",
               "status":"passed",
               "start":1540494392355,
               "stop":1540494392357
            },
            {  
               "name":"And Pet details are set as \"<pet_property>\" and \"<value>\"",
               "status":"passed",
               "attachments":[  
                  {  
                     "name":".table",
                     "source":"26b2cdbd-1d30-4c0b-9aae-51a5ae627f65-attachment.csv",
                     "type":"text/csv"
                  }
               ],
               "start":1540494392357,
               "stop":1540494392358
            },
            {  
               "name":"And Pet \"pending\" is specified",
               "status":"passed",
               "start":1540494392359,
               "stop":1540494392359
            },
            {  
               "name":"And Request BODY form parameters are set using pet details",
               "status":"passed",
               "start":1540494392359,
               "stop":1540494392359
            },
            {  
               "name":"And \"POST\" HTTP request is raised",
               "status":"passed",
               "start":1540494392359,
               "stop":1540494392840
            },
            {  
               "name":"Then Valid HTTP response is received",
               "status":"passed",
               "start":1540494392841,
               "stop":1540494392842
            },
            {  
               "name":"And Response http code is 200",
               "status":"passed",
               "start":1540494392842,
               "stop":1540494392843
            },
            {  
               "name":"And Response HEADER content type is \"application/json\"",
               "status":"passed",
               "start":1540494392843,
               "stop":1540494392843
            },
            {  
               "name":"And Response BODY is not null or empty",
               "status":"passed",
               "start":1540494392844,
               "stop":1540494392844
            },
            {  
               "name":"And Response BODY contains newly added pet details",
               "status":"broken",
               "statusDetails":{  
                  "message":"KeyError: 'status'\n",
                  "trace":"  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/model.py\", line 1329, in run\n    match.run(runner.context)\n  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/matchers.py\", line 98, in run\n    self.func(context, *args, **kwargs)\n  File \"features/steps/steps_pet.py\", line 69, in step_impl\n    assert_that(added_pet_json['status'], equal_to(context.pet.get_pet_status()))\n"
               },
               "start":1540494392844,
               "stop":1540494392847
            }
         ],
         "parameters":[  
            {  
               "name":"status",
               "value":"pending"
            }
         ],
         "start":1540494392351,
         "stop":1540494392847,
         "uuid":"2342973f-7ddb-417c-a729-18ca581ebfa6",
         "historyId":"a8851c23a0ab3cbbe5bb41035feb9c69",
         "labels":[  
            {  
               "name":"severity",
               "value":"normal"
            },
            {  
               "name":"feature",
               "value":"REST API Python and Behave testing framework"
            },
            {  
               "name":"framework",
               "value":"behave"
            },
            {  
               "name":"language",
               "value":"cpython3"
            }
         ]
      }
   },
   {  
      "Scenario_1":{  
         "name":"Add new pet using POST request -- @1.3 Pets",
         "status":"broken",
         "statusDetails":{  
            "message":"KeyError: 'status'\n",
            "trace":"  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/model.py\", line 1329, in run\n    match.run(runner.context)\n  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/matchers.py\", line 98, in run\n    self.func(context, *args, **kwargs)\n  File \"features/steps/steps_pet.py\", line 69, in step_impl\n    assert_that(added_pet_json['status'], equal_to(context.pet.get_pet_status()))\n"
         },
         "steps":[  
            {  
               "name":"Given Swagger PetStore web application url is set as \"https://petstore.swagger.io/v2/\"",
               "status":"passed",
               "start":1540494393287,
               "stop":1540494393288
            },
            {  
               "name":"Given \"POST\" api pet request endpoint is set as \"pet\"",
               "status":"passed",
               "start":1540494393288,
               "stop":1540494393289
            },
            {  
               "name":"When HEADER params for request and response are specified",
               "status":"passed",
               "start":1540494393289,
               "stop":1540494393291
            },
            {  
               "name":"And Pet details are set as \"<pet_property>\" and \"<value>\"",
               "status":"passed",
               "attachments":[  
                  {  
                     "name":".table",
                     "source":"7a5203d4-fa29-40f6-8f77-642fe195afda-attachment.csv",
                     "type":"text/csv"
                  }
               ],
               "start":1540494393292,
               "stop":1540494393293
            },
            {  
               "name":"And Pet \"sold\" is specified",
               "status":"passed",
               "start":1540494393294,
               "stop":1540494393294
            },
            {  
               "name":"And Request BODY form parameters are set using pet details",
               "status":"passed",
               "start":1540494393295,
               "stop":1540494393295
            },
            {  
               "name":"And \"POST\" HTTP request is raised",
               "status":"passed",
               "start":1540494393296,
               "stop":1540494393755
            },
            {  
               "name":"Then Valid HTTP response is received",
               "status":"passed",
               "start":1540494393756,
               "stop":1540494393756
            },
            {  
               "name":"And Response http code is 200",
               "status":"passed",
               "start":1540494393757,
               "stop":1540494393757
            },
            {  
               "name":"And Response HEADER content type is \"application/json\"",
               "status":"passed",
               "start":1540494393758,
               "stop":1540494393758
            },
            {  
               "name":"And Response BODY is not null or empty",
               "status":"passed",
               "start":1540494393759,
               "stop":1540494393759
            },
            {  
               "name":"And Response BODY contains newly added pet details",
               "status":"broken",
               "statusDetails":{  
                  "message":"KeyError: 'status'\n",
                  "trace":"  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/model.py\", line 1329, in run\n    match.run(runner.context)\n  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/matchers.py\", line 98, in run\n    self.func(context, *args, **kwargs)\n  File \"features/steps/steps_pet.py\", line 69, in step_impl\n    assert_that(added_pet_json['status'], equal_to(context.pet.get_pet_status()))\n"
               },
               "start":1540494393759,
               "stop":1540494393760
            }
         ],
         "parameters":[  
            {  
               "name":"status",
               "value":"sold"
            }
         ],
         "start":1540494393286,
         "stop":1540494393761,
         "uuid":"013b3623-c606-4c93-b418-0c2f5b5d0e20",
         "historyId":"0c432ef7339b3c914db9d37d4acaac80",
         "labels":[  
            {  
               "name":"severity",
               "value":"normal"
            },
            {  
               "name":"feature",
               "value":"REST API Python and Behave testing framework"
            },
            {  
               "name":"framework",
               "value":"behave"
            },
            {  
               "name":"language",
               "value":"cpython3"
            }
         ]
      }
   },
   {  
      "Scenario_2":{  
         "name":"Add new pet using POST request -- @1.2 Pets",
         "status":"broken",
         "statusDetails":{  
            "message":"KeyError: 'status'\n",
            "trace":"  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/model.py\", line 1329, in run\n    match.run(runner.context)\n  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/matchers.py\", line 98, in run\n    self.func(context, *args, **kwargs)\n  File \"features/steps/steps_pet.py\", line 69, in step_impl\n    assert_that(added_pet_json['status'], equal_to(context.pet.get_pet_status()))\n"
         },
         "steps":[  
            {  
               "name":"Given Swagger PetStore web application url is set as \"https://petstore.swagger.io/v2/\"",
               "status":"passed",
               "start":1540494392850,
               "stop":1540494392850
            },
            {  
               "name":"Given \"POST\" api pet request endpoint is set as \"pet\"",
               "status":"passed",
               "start":1540494392851,
               "stop":1540494392851
            },
            {  
               "name":"When HEADER params for request and response are specified",
               "status":"passed",
               "start":1540494392851,
               "stop":1540494392852
            },
            {  
               "name":"And Pet details are set as \"<pet_property>\" and \"<value>\"",
               "status":"passed",
               "attachments":[  
                  {  
                     "name":".table",
                     "source":"07cf281a-31be-4cbf-8ffc-cc572e02c800-attachment.csv",
                     "type":"text/csv"
                  }
               ],
               "start":1540494392853,
               "stop":1540494392853
            },
            {  
               "name":"And Pet \"available\" is specified",
               "status":"passed",
               "start":1540494392854,
               "stop":1540494392854
            },
            {  
               "name":"And Request BODY form parameters are set using pet details",
               "status":"passed",
               "start":1540494392854,
               "stop":1540494392854
            },
            {  
               "name":"And \"POST\" HTTP request is raised",
               "status":"passed",
               "start":1540494392855,
               "stop":1540494393278
            },
            {  
               "name":"Then Valid HTTP response is received",
               "status":"passed",
               "start":1540494393278,
               "stop":1540494393279
            },
            {  
               "name":"And Response http code is 200",
               "status":"passed",
               "start":1540494393279,
               "stop":1540494393279
            },
            {  
               "name":"And Response HEADER content type is \"application/json\"",
               "status":"passed",
               "start":1540494393280,
               "stop":1540494393280
            },
            {  
               "name":"And Response BODY is not null or empty",
               "status":"passed",
               "start":1540494393281,
               "stop":1540494393281
            },
            {  
               "name":"And Response BODY contains newly added pet details",
               "status":"broken",
               "statusDetails":{  
                  "message":"KeyError: 'status'\n",
                  "trace":"  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/model.py\", line 1329, in run\n    match.run(runner.context)\n  File \"/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/behave/matchers.py\", line 98, in run\n    self.func(context, *args, **kwargs)\n  File \"features/steps/steps_pet.py\", line 69, in step_impl\n    assert_that(added_pet_json['status'], equal_to(context.pet.get_pet_status()))\n"
               },
               "start":1540494393282,
               "stop":1540494393282
            }
         ],
         "parameters":[  
            {  
               "name":"status",
               "value":"available"
            }
         ],
         "start":1540494392849,
         "stop":1540494393283,
         "uuid":"39de3aba-c008-48ab-b1ef-b8944bb7914e",
         "historyId":"c2e2f01b0abe99b1c744e4a421d3a183",
         "labels":[  
            {  
               "name":"severity",
               "value":"normal"
            },
            {  
               "name":"feature",
               "value":"REST API Python and Behave testing framework"
            },
            {  
               "name":"framework",
               "value":"behave"
            },
            {  
               "name":"language",
               "value":"cpython3"
            }
         ]
      }
   }
]
file_name = "./results/" + str(datetime.now().strftime("%Y_%m_%d_%H%M_pet_store_api_report.html"))
if not os.path.exists(os.path.dirname(file_name)):
    try:
        os.makedirs(os.path.dirname(file_name))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
output = open(file_name, "wb")
#output.write(report)
gener = ReportGenerator(stream = output)
# print(gener.get_attributes(json))
#results = gener.get_attributes(json)
report = gener.generateReport(json)


