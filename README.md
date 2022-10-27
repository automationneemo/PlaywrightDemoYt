This repository is created for Playwright Learning purpose.

Pytest CLI commands:
Re run last failed tests only:
pytest --lf

Re-run all tests starting with failed tests:
pytest --ff

Stop at first failure:
pytest -x

Run a single test or using keyword:
pytest -k "login"

Allow maximum failure before stopping:
pytest --maxfail=2

pytest -s -v --headed --base-url=https://www.saucedemo.com --html=Report/
myreport.html --self-contained-html --capture=tee-sys --slowmo=600 --browser-channel=chrome

pytest --headed --browser-channel=chrome .\pytest_fw\test_01_sauce_demo.p
y::test_04_login_with_different_credentials              





