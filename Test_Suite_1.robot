*** Settings ***
Library           OperatingSystem

*** Test Cases ***
deleteTC
    ${output}    execute delete request test and return outcome
    Should Contain    ${output}    OK

getTC
    ${output}    execute get request test and return outcome
    Should Contain    ${output}    OK

patchTC
    ${output}    execute patch request test and return outcome
    Should Contain    ${output}    OK

putTC
    ${output}    execute put request test and return outcome
    Should Contain    ${output}    OK

postTC
    ${output}    execute post request test and return outcome
    Should Contain    ${output}    FAIL

*** Keywords ***
execute delete request test and return outcome
    ${output}    run    python -m unittest Testing\\test_delete_requests.py
    [Return]    ${output}

execute get request test and return outcome
    ${output}    run    python -m unittest Testing\\test_get_requests.py
    [Return]    ${output}

execute patch request test and return outcome
    ${output}    run    python -m unittest Testing\\test_patch_requests.py
    [Return]    ${output}

execute put request test and return outcome
    ${output}    run    python -m unittest Testing\\test_put_requests.py
    [Return]    ${output}

execute post request test and return outcome
    ${output}    run    python -m unittest Testing\\test_post_requests.py
    [Return]    ${output}
