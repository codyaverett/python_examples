# Flask

Flask is a super quick and easy to set up application server.

Use it for REST web applications. 

```shell
pipenv install
flask run # will automatically look for an app.py or wsgi.py file
flask --app hello
```

Navigate to the route or use curl to see the api output.

```shell
curl http://127.0.0.1:5000
```

## Reference
- [Documentation](https://flask.palletsprojects.com/en/2.2.x/)

## Run in app shell context

Explore the state of an actively running app context.

```shell
~/Projects/play/python_examples/flask (main*) » flask shell
Python 3.9.12 (main, Mar 26 2022, 15:44:31)
[Clang 13.1.6 (clang-1316.0.21.2)] on darwin
App: wsgi
Instance: /Users/caavere/Projects/play/python_examples/flask/instance
>>> dir()
['__builtins__', 'app', 'g']
>>> dir(app)
['__annotations__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_before_request_lock', '_check_setup_finished', '_find_error_handler', '_get_exc_class_and_code', '_got_first_request', '_json_decoder', '_json_encoder', '_method_route', '_static_folder', '_static_url_path', 'aborter', 'aborter_class', 'add_template_filter', 'add_template_global', 'add_template_test', 'add_url_rule', 'after_request', 'after_request_funcs', 'app_context', 'app_ctx_globals_class', 'async_to_sync', 'auto_find_instance_path', 'before_first_request', 'before_first_request_funcs', 'before_request', 'before_request_funcs', 'blueprints', 'cli', 'config', 'config_class', 'context_processor', 'create_global_jinja_loader', 'create_jinja_environment', 'create_url_adapter', 'debug', 'default_config', 'delete', 'dispatch_request', 'do_teardown_appcontext', 'do_teardown_request', 'endpoint', 'ensure_sync', 'env', 'error_handler_spec', 'errorhandler', 'extensions', 'finalize_request', 'full_dispatch_request', 'get', 'get_send_file_max_age', 'got_first_request', 'handle_exception', 'handle_http_exception', 'handle_url_build_error', 'handle_user_exception', 'has_static_folder', 'import_name', 'inject_url_defaults', 'instance_path', 'iter_blueprints', 'jinja_env', 'jinja_environment', 'jinja_loader', 'jinja_options', 'json', 'json_decoder', 'json_encoder', 'json_provider_class', 'log_exception', 'logger', 'make_aborter', 'make_config', 'make_default_options_response', 'make_response', 'make_shell_context', 'name', 'open_instance_resource', 'open_resource', 'patch', 'permanent_session_lifetime', 'post', 'preprocess_request', 'process_response', 'propagate_exceptions', 'put', 'raise_routing_exception', 'redirect', 'register_blueprint', 'register_error_handler', 'request_class', 'request_context', 'response_class', 'root_path', 'route', 'run', 'secret_key', 'select_jinja_autoescape', 'send_file_max_age_default', 'send_static_file', 'session_cookie_name', 'session_interface', 'shell_context_processor', 'shell_context_processors', 'should_ignore_error', 'static_folder', 'static_url_path', 'subdomain_matching', 'teardown_appcontext', 'teardown_appcontext_funcs', 'teardown_request', 'teardown_request_funcs', 'template_context_processors', 'template_filter', 'template_folder', 'template_global', 'template_test', 'templates_auto_reload', 'test_cli_runner', 'test_cli_runner_class', 'test_client', 'test_client_class', 'test_request_context', 'testing', 'trap_http_exception', 'update_template_context', 'url_build_error_handlers', 'url_default_functions', 'url_defaults', 'url_for', 'url_map', 'url_map_class', 'url_rule_class', 'url_value_preprocessor', 'url_value_preprocessors', 'use_x_sendfile', 'view_functions', 'wsgi_app']
```

