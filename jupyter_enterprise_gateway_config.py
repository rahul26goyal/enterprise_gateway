# Configuration file for jupyter-enterprise-gateway.
## Port on which to listen (EG_PORT env var)
#  Default: 8888
c.EnterpriseGatewayApp.port = 18888

## Set the log level by value or name.
#  Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
#  Default: 30
c.Application.log_level = 'DEBUG'

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## This is an application.

## The date format used by logging formatters for %(asctime)s
#  Default: '%Y-%m-%d %H:%M:%S'
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  Default: '[%(name)s]%(highlevel)s %(message)s'
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
#  Default: 30
# c.Application.log_level = 30

## Instead of starting the Application, dump configuration to stdout
#  Default: False
# c.Application.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  Default: False
# c.Application.show_config_json = False

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------
## Base class for Jupyter applications

## Answer yes to any prompts.
#  Default: False
# c.JupyterApp.answer_yes = False

## Full path of a config file.
#  Default: ''
# c.JupyterApp.config_file = ''

## Specify a config file to load.
#  Default: ''
# c.JupyterApp.config_file_name = ''

## Generate default config file.
#  Default: False
# c.JupyterApp.generate_config = False

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.JupyterApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.JupyterApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.JupyterApp.log_level = 30

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.JupyterApp.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.JupyterApp.show_config_json = False

#------------------------------------------------------------------------------
# EnterpriseGatewayApp(JupyterApp) configuration
#------------------------------------------------------------------------------
## Application that provisions Jupyter kernels and proxies HTTP/Websocket
#      traffic to the kernels.
#  
#      - reads command line and environment variable settings
#      - initializes managers and routes
#      - creates a Tornado HTTP server
#      - starts the Tornado event loop

## Sets the Access-Control-Allow-Credentials header. (EG_ALLOW_CREDENTIALS env
#  var)
#  Default: ''
# c.EnterpriseGatewayApp.allow_credentials = ''

## Sets the Access-Control-Allow-Headers header. (EG_ALLOW_HEADERS env var)
#  Default: ''
# c.EnterpriseGatewayApp.allow_headers = ''

## Sets the Access-Control-Allow-Methods header. (EG_ALLOW_METHODS env var)
#  Default: ''
# c.EnterpriseGatewayApp.allow_methods = ''

## Sets the Access-Control-Allow-Origin header. (EG_ALLOW_ORIGIN env var)
#  Default: ''
# c.EnterpriseGatewayApp.allow_origin = ''

## The http url specifying the alternate YARN Resource Manager.  This value should
#                                  be set when YARN Resource Managers are configured for high availability.  Note: If both
#                                  YARN endpoints are NOT set, the YARN library will use the files within the local
#                                  HADOOP_CONFIG_DIR to determine the active resource manager.
#                                  (EG_ALT_YARN_ENDPOINT env var)
#  Default: None
# c.EnterpriseGatewayApp.alt_yarn_endpoint = None

## Answer yes to any prompts.
#  See also: JupyterApp.answer_yes
# c.EnterpriseGatewayApp.answer_yes = False

## Authorization token required for all requests (EG_AUTH_TOKEN env var)
#  Default: ''
# c.EnterpriseGatewayApp.auth_token = ''

## Comma-separated list of user names (e.g., ['bob','alice']) against which
#                             KERNEL_USERNAME will be compared.  Any match (case-sensitive) will allow the kernel's
#                             launch, otherwise an HTTP 403 (Forbidden) error will be raised.  The set of unauthorized
#                             users takes precedence. This option should be used carefully as it can dramatically limit
#                             who can launch kernels.  (EG_AUTHORIZED_USERS env var - non-bracketed,
#                             just comma-separated)
#  Default: set()
# c.EnterpriseGatewayApp.authorized_users = set()

## The base path for mounting all API resources (EG_BASE_URL env var)
#  Default: '/'
# c.EnterpriseGatewayApp.base_url = '/'

## The full path to an SSL/TLS certificate file. (EG_CERTFILE env var)
#  Default: None
# c.EnterpriseGatewayApp.certfile = None

## The full path to a certificate authority certificate for SSL/TLS
#                          client authentication. (EG_CLIENT_CA env var)
#  Default: None
# c.EnterpriseGatewayApp.client_ca = None

## The http url for accessing the Conductor REST API.
#                                   (EG_CONDUCTOR_ENDPOINT env var)
#  Default: None
# c.EnterpriseGatewayApp.conductor_endpoint = None

## Full path of a config file.
#  See also: JupyterApp.config_file
# c.EnterpriseGatewayApp.config_file = ''

## Specify a config file to load.
#  See also: JupyterApp.config_file_name
# c.EnterpriseGatewayApp.config_file_name = ''

## Default kernel name when spawning a kernel (EG_DEFAULT_KERNEL_NAME env var)
#  Default: ''
# c.EnterpriseGatewayApp.default_kernel_name = ''

## Specifies the number of seconds configuration files are polled for
#                                        changes.  A value of 0 or less disables dynamic config updates.
#                                        (EG_DYNAMIC_CONFIG_INTERVAL env var)
#  Default: 0
# c.EnterpriseGatewayApp.dynamic_config_interval = 0

## Environment variables allowed to be inherited
#                                   from the spawning process by the kernel. (EG_ENV_PROCESS_WHITELIST env var)
#  Default: []
# c.EnterpriseGatewayApp.env_process_whitelist = []

## Environment variables allowed to be set when a client requests a
#                           new kernel. (EG_ENV_WHITELIST env var)
#  Default: []
# c.EnterpriseGatewayApp.env_whitelist = []

## Sets the Access-Control-Expose-Headers header. (EG_EXPOSE_HEADERS env var)
#  Default: ''
# c.EnterpriseGatewayApp.expose_headers = ''

## Generate default config file.
#  See also: JupyterApp.generate_config
# c.EnterpriseGatewayApp.generate_config = False

## Indicates whether impersonation will be performed during kernel launch.
#                                   (EG_IMPERSONATION_ENABLED env var)
#  Default: False
# c.EnterpriseGatewayApp.impersonation_enabled = False

## IP address on which to listen (EG_IP env var)
#  Default: '127.0.0.1'
# c.EnterpriseGatewayApp.ip = '127.0.0.1'

## The kernel manager class to use. Must be a subclass of
#  `notebook.services.kernels.MappingKernelManager`.
#  Default: 'enterprise_gateway.services.kernels.remotemanager.RemoteMappingKernelManager'
# c.EnterpriseGatewayApp.kernel_manager_class = 'enterprise_gateway.services.kernels.remotemanager.RemoteMappingKernelManager'

## The kernel session manager class to use. Must be a subclass of
#  `enterprise_gateway.services.sessions.KernelSessionManager`.
#  Default: 'enterprise_gateway.services.sessions.kernelsessionmanager.FileKernelSessionManager'
# c.EnterpriseGatewayApp.kernel_session_manager_class = 'enterprise_gateway.services.sessions.kernelsessionmanager.FileKernelSessionManager'

## The kernel spec manager class to use. Must be a subclass of
#  `jupyter_client.kernelspec.KernelSpecManager`.
#  Default: 'jupyter_client.kernelspec.KernelSpecManager'
# c.EnterpriseGatewayApp.kernel_spec_manager_class = 'jupyter_client.kernelspec.KernelSpecManager'

## The full path to a private key file for usage with SSL/TLS. (EG_KEYFILE env
#  var)
#  Default: None
# c.EnterpriseGatewayApp.keyfile = None

## Permits listing of the running kernels using API endpoints /api/kernels
#                          and /api/sessions. (EG_LIST_KERNELS env var) Note: Jupyter Notebook
#                          allows this by default but Jupyter Enterprise Gateway does not.
#  Default: False
# c.EnterpriseGatewayApp.list_kernels = False

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.EnterpriseGatewayApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.EnterpriseGatewayApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.EnterpriseGatewayApp.log_level = 30

## Sets the Access-Control-Max-Age header. (EG_MAX_AGE env var)
#  Default: ''
# c.EnterpriseGatewayApp.max_age = ''

## Limits the number of kernel instances allowed to run by this gateway.
#                            Unbounded by default. (EG_MAX_KERNELS env var)
#  Default: None
# c.EnterpriseGatewayApp.max_kernels = None

## Specifies the maximum number of kernels a user can have active
#                                     simultaneously.  A value of -1 disables enforcement.
#                                     (EG_MAX_KERNELS_PER_USER env var)
#  Default: -1
# c.EnterpriseGatewayApp.max_kernels_per_user = -1

## Port on which to listen (EG_PORT env var)
#  Default: 8888
# c.EnterpriseGatewayApp.port = 8888

## Specifies the lower and upper port numbers from which ports are created.
#                           The bounded values are separated by '..' (e.g., 33245..34245 specifies a range of 1000 ports
#                           to be randomly selected). A range of zero (e.g., 33245..33245 or 0..0) disables port-range
#                           enforcement.  (EG_PORT_RANGE env var)
#  Default: '0..0'
# c.EnterpriseGatewayApp.port_range = '0..0'

## Number of ports to try if the specified port is not available
#                             (EG_PORT_RETRIES env var)
#  Default: 50
# c.EnterpriseGatewayApp.port_retries = 50

## Bracketed comma-separated list of hosts on which DistributedProcessProxy
#                          kernels will be launched e.g., ['host1','host2']. (EG_REMOTE_HOSTS env var
#                          - non-bracketed, just comma-separated)
#  Default: ['localhost']
# c.EnterpriseGatewayApp.remote_hosts = ['localhost']

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.EnterpriseGatewayApp.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.EnterpriseGatewayApp.show_config_json = False

## Use x-* header values for overriding the remote-ip, useful when
#                             application is behing a proxy. (EG_TRUST_XHEADERS env var)
#  Default: False
# c.EnterpriseGatewayApp.trust_xheaders = False

## Comma-separated list of user names (e.g., ['root','admin']) against which
#                               KERNEL_USERNAME will be compared.  Any match (case-sensitive) will prevent the
#                               kernel's launch and result in an HTTP 403 (Forbidden) error.
#                               (EG_UNAUTHORIZED_USERS env var - non-bracketed, just comma-separated)
#  Default: {'root'}
# c.EnterpriseGatewayApp.unauthorized_users = {'root'}

## Specifies the ping interval(in seconds) that should be used by zmq port
#                                       associated withspawned kernels.Set this variable to 0 to disable ping mechanism.
#                                      (EG_WS_PING_INTERVAL_SECS env var)
#  Default: 30
# c.EnterpriseGatewayApp.ws_ping_interval = 30

## The http url specifying the YARN Resource Manager. Note: If this value is NOT set,
#                              the YARN library will use the files within the local HADOOP_CONFIG_DIR to determine the
#                              active resource manager. (EG_YARN_ENDPOINT env var)
#  Default: None
# c.EnterpriseGatewayApp.yarn_endpoint = None

## Is YARN Kerberos/SPNEGO Security enabled (True/False).
#                                            (EG_YARN_ENDPOINT_SECURITY_ENABLED env var)
#  Default: False
# c.EnterpriseGatewayApp.yarn_endpoint_security_enabled = False

#------------------------------------------------------------------------------
# KernelSessionManager(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## KernelSessionManager is used to save and load kernel sessions from persistent
#  storage.
#  
#         KernelSessionManager provides the basis for an HA solution.  It loads the complete set of persisted kernel
#         sessions during construction.  Following construction the parent object calls start_sessions to allow
#         Enterprise Gateway to validate that all loaded sessions are still valid.  Those that it cannot 'revive'
#         are marked for deletion and the in-memory dictionary is updated - and the entire collection is written
#         to store (file or database).
#  
#         As kernels are created and destroyed, the KernelSessionManager is called upon to keep kernel session
#         state consistent.
#  
#         NOTE: This class is essentially an abstract base class that requires its `load_sessions` and `save_sessions`
#         have implementations in subclasses.  abc.MetaABC is not used due to conflicts with derivation of
#         LoggingConfigurable - which seemed more important.

## Enable kernel session persistence (True or False). Default = False
#                                (EG_KERNEL_SESSION_PERSISTENCE env var)
#  Default: False
# c.KernelSessionManager.enable_persistence = False

## Identifies the root 'directory' under which the 'kernel_sessions' node will
#                                 reside.  This directory should exist.  (EG_PERSISTENCE_ROOT env var)
#  Default: ''
# c.KernelSessionManager.persistence_root = ''

#------------------------------------------------------------------------------
# FileKernelSessionManager(KernelSessionManager) configuration
#------------------------------------------------------------------------------
## Performs kernel session persistence operations against the file
#  `sessions.json` located in the kernel_sessions directory in the directory
#  pointed to by the persistence_root parameter (default JUPYTER_DATA_DIR).

## Enable kernel session persistence (True or False). Default = False
#  See also: KernelSessionManager.enable_persistence
# c.FileKernelSessionManager.enable_persistence = False

## Identifies the root 'directory' under which the 'kernel_sessions' node will
#  See also: KernelSessionManager.persistence_root
# c.FileKernelSessionManager.persistence_root = ''

#------------------------------------------------------------------------------
# MultiKernelManager(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## A class for managing multiple kernels.

## The name of the default kernel to start
#  Default: 'python3'
# c.MultiKernelManager.default_kernel_name = 'python3'

## The kernel manager class.  This is configurable to allow
#          subclassing of the KernelManager for customized behavior.
#  Default: 'jupyter_client.ioloop.IOLoopKernelManager'
# c.MultiKernelManager.kernel_manager_class = 'jupyter_client.ioloop.IOLoopKernelManager'

## Share a single zmq.Context to talk to all my kernels
#  Default: True
# c.MultiKernelManager.shared_context = True

#------------------------------------------------------------------------------
# MappingKernelManager(MultiKernelManager) configuration
#------------------------------------------------------------------------------
## A KernelManager that handles notebook mapping and HTTP error handling

## White list of allowed kernel message types.
#          When the list is empty, all message types are allowed.
#  Default: []
# c.MappingKernelManager.allowed_message_types = []

## Whether messages from kernels whose frontends have disconnected should be
#  buffered in-memory.
#  
#          When True (default), messages are buffered and replayed on reconnect,
#          avoiding lost messages due to interrupted connectivity.
#  
#          Disable if long-running kernels will produce too much output while
#          no frontends are connected.
#  Default: True
# c.MappingKernelManager.buffer_offline_messages = True

## Whether to consider culling kernels which are busy.
#          Only effective if cull_idle_timeout > 0.
#  Default: False
# c.MappingKernelManager.cull_busy = False

## Whether to consider culling kernels which have one or more connections.
#          Only effective if cull_idle_timeout > 0.
#  Default: False
# c.MappingKernelManager.cull_connected = False

## Timeout (in seconds) after which a kernel is considered idle and ready to be culled.
#          Values of 0 or lower disable culling. Very short timeouts may result in kernels being culled
#          for users with poor network connections.
#  Default: 0
# c.MappingKernelManager.cull_idle_timeout = 0

## The interval (in seconds) on which to check for idle kernels exceeding the
#  cull timeout value.
#  Default: 300
# c.MappingKernelManager.cull_interval = 300

## The name of the default kernel to start
#  See also: MultiKernelManager.default_kernel_name
# c.MappingKernelManager.default_kernel_name = 'python3'

## Timeout for giving up on a kernel (in seconds).
#  
#          On starting and restarting kernels, we check whether the
#          kernel is running and responsive by sending kernel_info_requests.
#          This sets the timeout in seconds for how long the kernel can take
#          before being presumed dead.
#          This affects the MappingKernelManager (which handles kernel restarts)
#          and the ZMQChannelsHandler (which handles the startup).
#  Default: 60
# c.MappingKernelManager.kernel_info_timeout = 60

## The kernel manager class.  This is configurable to allow
#  See also: MultiKernelManager.kernel_manager_class
# c.MappingKernelManager.kernel_manager_class = 'jupyter_client.ioloop.IOLoopKernelManager'

#  Default: ''
# c.MappingKernelManager.root_dir = ''

## Share a single zmq.Context to talk to all my kernels
#  See also: MultiKernelManager.shared_context
# c.MappingKernelManager.shared_context = True

#------------------------------------------------------------------------------
# RemoteMappingKernelManager(MappingKernelManager) configuration
#------------------------------------------------------------------------------
## Extends the MappingKernelManager with support for managing remote kernels via
#  the process-proxy.

## White list of allowed kernel message types.
#  See also: MappingKernelManager.allowed_message_types
# c.RemoteMappingKernelManager.allowed_message_types = []

## Whether messages from kernels whose frontends have disconnected should be
#  buffered in-memory.
#  See also: MappingKernelManager.buffer_offline_messages
# c.RemoteMappingKernelManager.buffer_offline_messages = True

## Whether to consider culling kernels which are busy.
#  See also: MappingKernelManager.cull_busy
# c.RemoteMappingKernelManager.cull_busy = False

## Whether to consider culling kernels which have one or more connections.
#  See also: MappingKernelManager.cull_connected
# c.RemoteMappingKernelManager.cull_connected = False

## Timeout (in seconds) after which a kernel is considered idle and ready to be
#  culled.
#  See also: MappingKernelManager.cull_idle_timeout
# c.RemoteMappingKernelManager.cull_idle_timeout = 0

## The interval (in seconds) on which to check for idle kernels exceeding the
#  cull timeout value.
#  See also: MappingKernelManager.cull_interval
# c.RemoteMappingKernelManager.cull_interval = 300

## The name of the default kernel to start
#  See also: MultiKernelManager.default_kernel_name
# c.RemoteMappingKernelManager.default_kernel_name = 'python3'

## Timeout for giving up on a kernel (in seconds).
#  See also: MappingKernelManager.kernel_info_timeout
# c.RemoteMappingKernelManager.kernel_info_timeout = 60

## The kernel manager class.  This is configurable to allow
#  See also: MultiKernelManager.kernel_manager_class
# c.RemoteMappingKernelManager.kernel_manager_class = 'jupyter_client.ioloop.IOLoopKernelManager'

#  See also: MappingKernelManager.root_dir
# c.RemoteMappingKernelManager.root_dir = ''

## Share a single zmq.Context to talk to all my kernels
#  See also: MultiKernelManager.shared_context
# c.RemoteMappingKernelManager.shared_context = True
