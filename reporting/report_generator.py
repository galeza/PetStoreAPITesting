'''
Created on Oct 16, 2018

@author: agagaleza

New status was added - now test can be skipped.
Deatil button was corrected.
"""
A TestRunner for use with the Python unit testing framework. It
generates a HTML report to show the result at a glance.

The simplest way to use this is to invoke its main method. E.g.

    import unittest
    import HTMLTestRunner

    ... define your tests ...

    if __name__ == '__main__':
        HTMLTestRunner.main()


For more customization options, instantiates a HTMLTestRunner object.
HTMLTestRunner is a counterpart to unittest's TextTestRunner. E.g.

    # output to a file
    fp = file('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )

    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

    # run the test
    runner.run(my_test_suite)


------------------------------------------------------------------------
Copyright (c) 2004-2007, Wai Yip Tung
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name Wai Yip Tung nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# URL: http://tungwaiyip.info/software/HTMLTestRunner.html

__author__ = "Wai Yip Tung"

'''
from datetime import datetime
from xml.sax import saxutils
from reporting.html_report_constants import HtmlReportConstants
import logging
from reporting.report_constants import ReportConstants

class ReportGenerator(object):
    __version__ = "0.1"
    logger = logging.getLogger(__name__)
    '''
    classdocs
    '''
    


    def __init__(self,stream):
        self.title = HtmlReportConstants.DEFAULT_TITLE
        self.description = HtmlReportConstants.DEFAULT_DESCRIPTION
        self.stream = stream

    def get_attributes(self, json_data):
        start_time = datetime.utcnow()
        duration = 0
        try:
            start_time = json_data[0][ReportConstants.SCENARIO + '0'][ReportConstants.START]
            self.logger.info(self.format_unix_timestamp(start_time / 1000, '%Y-%m-%d %H:%M:%S'))
            end_time = int(json_data[-1][ReportConstants.SCENARIO+ str(len(json_data) - 1)][ReportConstants.STOP])
            self.logger.info(self.format_unix_timestamp(end_time / 1000, '%Y-%m-%d %H:%M:%S'))
            duration = end_time - start_time
            self.logger.info(duration)
            counters = {ReportConstants.PASSED:0, ReportConstants.FAILED:0, ReportConstants.SKIPPED:0, ReportConstants.ERROR:0}
            
            status = []

            for x in json_data:
                for scenario in x:
                    result = HtmlReportConstants.STATUS[x[scenario][ReportConstants.STATUS]]
                    counters[result] +=1

            for cnt in counters:
                status.append(cnt.title() + ' %s' % counters[cnt])


            if status:
                status = ' '.join(status)
            else:
                status = 'none'
        except KeyError:
            self.logger.info('Empty results')
        except IndexError:
            self.logger.info('Empty results')
        self.logger.info(self.convert_miliseconds(duration))
        return [
            ('Start Time', self.format_unix_timestamp(start_time / 1000, '%Y-%m-%d %H:%M:%S')),
            ('Duration', str(self.convert_miliseconds(duration))),
            ('Status', status),
        ]

    def generate_report(self, result):
        report_attrs = self.get_attributes(result)
        generator = 'ReportGenerator %s' % ReportGenerator.__version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        output = HtmlReportConstants.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator = generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            ending=ending,
        )
        self.stream.write(output.encode('utf8'))
        
    def _generate_stylesheet(self):
        return HtmlReportConstants.STYLESHEET_TMPL
    
    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            self.logger.info('name ' + str(name))
            self.logger.info('value' + str(value))
            line = HtmlReportConstants.HEADING_ATTRIBUTE_TMPL % dict(
                    name=saxutils.escape(name),
                    value=saxutils.escape(value),
                )
            a_lines.append(line)
        heading = HtmlReportConstants.HEADING_TMPL % dict(
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
        total_skipped = 0
        for scenario in json_data:
            counters = {ReportConstants.PASSED:0, ReportConstants.FAILED:0, ReportConstants.SKIPPED:0, ReportConstants.ERROR:0}
            for step in scenario[ReportConstants.SCENARIO + str(scenario_id)][ReportConstants.STEPS]:
                counters[step[ReportConstants.STATUS]] +=1

            row = HtmlReportConstants.REPORT_CLASS_TMPL % dict(
                style=counters[ReportConstants.ERROR] > 0 and 'errorClass' or counters[ReportConstants.SKIPPED] > 0 and 'skippedClass'or counters[ReportConstants.FAILED] > 0 and 'failClass' or 'passClass',
                desc=scenario[ReportConstants.SCENARIO + str(scenario_id)][ReportConstants.NAME],
                count=sum(counters.values()),
                Pass=counters[ReportConstants.PASSED],
                fail=counters[ReportConstants.FAILED],
                error=counters[ReportConstants.ERROR],
                skipped = counters[ReportConstants.SKIPPED],
                cid='c%s' % (scenario_id + 1),
            )
            rows.append(row)
            step_id = 1
            for step in scenario[ReportConstants.SCENARIO + str(scenario_id)][ReportConstants.STEPS]:
                self._generate_report_test(rows, scenario_id,step, step_id, step_id)
                step_id +=1
            scenario_id +=  1
            total_passed +=counters[ReportConstants.PASSED]
            total_failed += counters[ReportConstants.FAILED]
            total_error += counters[ReportConstants.ERROR]
            total_skipped +=counters[ReportConstants.SKIPPED]
        report = HtmlReportConstants.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(total_passed + total_failed + total_error),
            Pass=str(total_passed),
            fail=str(total_failed),
            error=str(total_error),
            skipped = str(total_skipped)
            )
          
        return report

    def _generate_report_test(self, rows, cid,step, tid, name):
        status = HtmlReportConstants.STATUS[step[ReportConstants.STATUS]]
        has_output = bool(status != ReportConstants.PASSED and status != ReportConstants.SKIPPED)
        tid = status + ' t%s.%s' % (cid+1,tid)
        doc = step[ReportConstants.NAME]
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and HtmlReportConstants.REPORT_TEST_WITH_OUTPUT_TMPL or HtmlReportConstants.REPORT_TEST_NO_OUTPUT_TMPL
        uo = ''
        ue = ''
        try:
            uo = step[ReportConstants.STATUS_DETAILS][ReportConstants.MESSAGE]
            ue = step[ReportConstants.STATUS_DETAILS][ReportConstants.TRACE]
        except KeyError:
            pass

        script = HtmlReportConstants.REPORT_TEST_OUTPUT_TMPL % dict(
            id = tid,
            output = saxutils.escape(uo+ue),
        )
        class_str = 'none'
        if status == "passed":
            class_str = 'hiddenRow'
            
        style_str = 'none'
        if status == 'failed':
            style_str = 'failCase'
        elif status == 'skipped':
            style_str = 'skippedCase'
            class_str = 'hiddenRow'
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
        return HtmlReportConstants.ENDING_TMPL

    def format_unix_timestamp(self, unixtime, formatstr):
        return str(datetime.utcfromtimestamp(unixtime).strftime(formatstr))   


    def convert_miliseconds(self, ms):
        s=ms/1000
        m,s=divmod(s,60)
        h,m=divmod(m,60)
        d,h=divmod(h,24)
        
        return "%d days %02d:%02d:%02d" % (d,h,m,s) 
    




