'''
Created on Sep 7, 2018

@author: agagaleza
'''

import glob
import sys
import os
from shutil import rmtree
from behave import __main__ as runner_with_options
import json
from reporting.report_generator import ReportGenerator
from datetime import datetime
import collections

if __name__ == '__main__':
    sys.stdout.flush()
    test_date = str(datetime.now().strftime("%Y_%m_%d_%H%M"))
    reporting_folder_name = './reporting/results/' + test_date
    #
    # remove if any reporting folder exists
    if os.path.exists(reporting_folder_name):
        rmtree(reporting_folder_name)
    os.makedirs(reporting_folder_name)
#     os.chdir('./features')
    #
    # allure reporting related command line arguments
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o ' + reporting_folder_name + '  '
    #
    # feature file path
    #for console
    featureFilePath = './features/feature_pet/ '
    #for eclipse
#     featureFilePath = 'Pet_Store_API_Testing.feature'
    #
    # tag option (currently not using any tag)
    tagOptions = ' --tags=-tag_me '
    tagOptions = ''
    #
    # command line argument to capture console output
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    #
    # full list of command line options
    print(os.getcwd())
    fullRunnerOptions = tagOptions + featureFilePath + reportingRelated + commonRunnerOptions
    #
    # run Behave + BDD + Python code
    runner_with_options.main(fullRunnerOptions)
    #
#     os.chdir('..')
    # read resultant json file
    listOfJsonFiles = glob.glob(reporting_folder_name + "/*.json")
    finalJson = ''
    scenario_dict = {}
    for cnt in range(0, len(listOfJsonFiles)):
        scenario_data = json.loads(open(listOfJsonFiles[cnt], 'r').read())
        start_time = int(scenario_data['start'])
        scenario_dict[start_time] = scenario_data

#         listOfJsonFiles[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJsonFiles[cnt], 'r').read() + '}'
#         if cnt < (-1 + len(listOfJsonFiles)):
#             listOfJsonFiles[cnt] = listOfJsonFiles[cnt] + ','
#         finalJson = finalJson + listOfJsonFiles[cnt]
#     finalJson = '[ ' + finalJson + ' ]'
    data = []
    index = 0
    for start_time in collections.OrderedDict(sorted(scenario_dict.items())):
        print(start_time)
        print(scenario_dict[start_time]['name'])
        scenario_data = {}
        scenario_data["Scenario_" + str(index)] = scenario_dict[start_time]
        data.append(scenario_data)
        index +=1
        
    # for  scen in sorted 
    #    new dict scenario/-dict["Scenario_" + str(cnt) + '"] = scenrio
    #    append to new array
    #
    # convert json to html using simple utility and publish report
#     html_content = json2html.convert(json=finalJson)
#     data = json.loads(finalJson)
#     print(isinstance(data, list))
#     print(data)
#     print(data)
    output = open(reporting_folder_name + '/' + str(datetime.now().strftime("%Y_%m_%d_%H%M_pet_store_api_report.html")), 'wb')
    generator = ReportGenerator(stream = output)
    report = generator.generateReport(data)
#     html_report_file.write(html_content)
#     html_report_file.close()
#     HTMLTestRunner.HTMLTestRunner(stream = html_report_file, verbosity = 2, title="SmsEagle API Regression Suite")