'''
Created on Sep 7, 2018

@author: agagaleza
'''

import glob
from json2html import *
import sys
import os
from shutil import rmtree
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    reporting_folder_name = 'reporting_folder_json_html'
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
    for cnt in range(0, len(listOfJsonFiles)):
        listOfJsonFiles[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJsonFiles[cnt], 'r').read() + '}'
        if cnt < (-1 + len(listOfJsonFiles)):
            listOfJsonFiles[cnt] = listOfJsonFiles[cnt] + ','
        finalJson = finalJson + listOfJsonFiles[cnt]
    finalJson = '[ ' + finalJson + ' ]'
    #
    # convert json to html using simple utility and publish report
    html_content = json2html.convert(json=finalJson)
    html_report_file = open(reporting_folder_name + '/' + 'index.html', 'w')
    html_report_file.write(html_content)
    html_report_file.close()