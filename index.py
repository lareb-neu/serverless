from botocore.exceptions import ClientError
import json
import boto3
def handler(event, context):
    username=json.loads(event['Records'][0]['Sns']['Message'])['Username']
    token=json.loads(event['Records'][0]['Sns']['Message'])['Subject']
    messagetype=json.loads(event['Records'][0]['Sns']['Message'])['MessageType']
    send_email(username, token, messagetype)
def send_email(email,token, messagetype):
    SENDER = "employeease@demo.larebkhan.me"

    RECIPIENT = email

    authlink = "http://demo.larebkhan.me/v1/verify?email=" + email + "&token=" + token

    print(authlink)


    DESTINATION = {
        'ToAddresses': [
            RECIPIENT,
        ]
    }

    AWS_REGION = "us-east-1"

    SUBJECT = messagetype+" for candidate account"

    BODY_TEXT = ("We need to verify your account to move further\r\n"
                 "Details:\r\n"
                 "\n"
                 "Hello " + email + "\n"
                 "\n"
                 "Verifying email id: " + email + "\r\n"
                 "\r\n"
                 "Click this link to confirm your email address and complete setup for your candidate account. This link will expire in 5 minutes\r\n"
                 "Verify: " + authlink
                 )

    CHARSET = "UTF-8"
    
    client = boto3.client('ses')
    try:
        response = client.send_email(
            Destination=DESTINATION,
            Message={
                'Body': {
                    # 'Html': {
                    #     'Charset': CHARSET,
                    #     'Data': BODY_,
                    # },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
         )

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:")
        print(response['MessageId'])
        print(RECIPIENT)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }