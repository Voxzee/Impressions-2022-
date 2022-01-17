from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTThingJobsClient

# For certificate based connection
myJobsClient = AWSIoTMQTTThingJobsClient("myClientID", "myThingName")
# For Websocket connection
# myJobsClient = AWSIoTMQTTThingJobsClient("myClientID", "myThingName", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myJobsClient.configureEndpoint("YOUR.ENDPOINT", 8883)
# For Websocket
# myJobsClient.configureEndpoint("YOUR.ENDPOINT", 443)
myJobsClient.configureCredentials("YOUR/ROOT/CA/PATH", "PRIVATE/KEY/PATH", "CERTIFICATE/PATH")
# For Websocket, we only need to configure the root CA
# myJobsClient.configureCredentials("YOUR/ROOT/CA/PATH")
myJobsClient.configureConnectDisconnectTimeout(10)  # 10 sec
myJobsClient.configureMQTTOperationTimeout(5)  # 5 sec
...

