def pytest_configure(config):
    config.addinivalue_line(
        'markers', 'smoke: tests for smoke testing, auth: tests for auth'
    )
    config.addinivalue_line(
        'markers', 'auth: tests for auth'
    )