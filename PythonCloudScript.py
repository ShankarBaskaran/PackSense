from pusher_push_notifications import PushNotifications
import pyrebase
config = {
'apiKey': "AIzaSyAqRh6LBj9GNWTfd__YrWm_2w4jc2qMUbQ",
'authDomain': "my-project-1557998794910.firebaseapp.com",
'databaseURL': "https://my-project-1557998794910.firebaseio.com",
'projectId': "my-project-1557998794910",
'storageBucket': "my-project-1557998794910.appspot.com",
'messagingSenderId': "796700778357"
}
firebase = pyrebase.initialize_app(config)
db=firebase.database()
pn_client = PushNotifications(
instance_id='e264a63f-7566-4bc9-9bd3-f01cfd1c9947',
secret_key='E121B518642861E893038924900F118C2BD609B2BDF7AEEF460D1CF2565CB86E',
)
def stream_handler(message):
 print(message)
 if(message['path'] == "/HUMIDITY"):
  if(float(message['data']) > 70.00):
   response = pn_client.publish(
   interests=['hello'],
   publish_body={
    'apns': {
     'aps': {
      'alert': 'ALERT',
      },
     },
     'fcm': {
      'notification': {
       'title': 'Humidity is increasing',
       'body': 'Please check ASAP',
      },
     },
    },
   )
   print(response['publishId'])
 if(message['path'] == "/SHOCK"):
    if(int(message['data']) > 0):
     response = pn_client.publish(
     interests=['hello'],
     publish_body={
      'apns': {
       'aps': {
        'alert': 'ALERT',
        },
       },
       'fcm': {
        'notification': {
         'title': 'High Vibrations/Misplacements',
         'body': 'Please reduce it',
        },
       },
      },
     )
     print(response['publishId'])
 if(message['path'] == "/LUMINOUS"):
  if(int(message['data']) < 1024):
   response = pn_client.publish(
   interests=['hello'],
   publish_body={
    'apns': {
     'aps': {
      'alert': 'ALERT',
      },
     },
     'fcm': {
      'notification': {
       'title': 'The box is opened',
       'body': 'Please check ASAP',
      },
     },
    },
   )
   print(response['publishId'])
 if(message['path'] == "/TEMPERATURE"):
  if(float(message['data']) > 33.00):
   response = pn_client.publish(
   interests=['hello'],
   publish_body={
    'apns': {
     'aps': {
      'alert': 'ALERT',
      },
     },
     'fcm': {
      'notification': {
       'title': 'Temperature is rising',
       'body': 'Please check ASAP',
      },
     },
    },
   )
   print(response['publishId'])
my_stream = db.child().stream(stream_handler,None)

