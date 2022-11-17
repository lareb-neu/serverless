from botocore.exceptions import ClientError
import json
import boto3
def handler(event, context):
    username=json.loads(event['Records'][0]['Sns']['Message'])['Username']
    token=json.loads(event['Records'][0]['Sns']['Message'])['Subject']
    send_email(username, token)

def send_email(email,token):
    SENDER = "no-reply@demo.larebkhan.me"

    RECIPIENT = email

    authlink = "http://demo.larebkhan.me/verify?email=" + email + "&token=" + token

    print(authlink)


    DESTINATION = {
        'ToAddresses': [
            RECIPIENT,
        ]
    }

    AWS_REGION = "us-east-1"

    SUBJECT = "Verification Email"

    BODY_TEXT = ("Email verification for new user\r\n"
                 "Details:\r\n"
                 "\n"
                 "Name: " + email + "\n"
                 "\n"
                 "Verifying email id: " + email + "\r\n"
                 "\r\n"
                 "Use the link provided below to verify yourself:\r\n"
                 "Verify: " + authlink
                 )

    CHARSET = "UTF-8"
    
    client = boto3.client('ses', region_name='us-east-1',aws_access_key_id='AKIAZAXXVSVN3BCKCQMV',
                                  aws_secret_access_key='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')

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