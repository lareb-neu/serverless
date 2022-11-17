import json
import boto3

def lambda_handler(event, context):
    
    ses = boto3.client('ses')

    body = """
	    Hello and welcome to the SES Lambda Python Demo.
	
	    Regards,
	    NKT Studios
    """

    ses.send_email(
	    Source = 'noreply@demo.larebkhan.me',
	    Destination = {
		    'ToAddresses': [
			    'larebkhan96@gmail.com'
		    ]
	    },
	    Message = {
		    'Subject': {
			    'Data': 'SES Demo',
			    'Charset': 'UTF-8'
		    },
		    'Body': {
			    'Text':{
				    'Data': body,
				    'Charset': 'UTF-8'
			    }
		    }
	    }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent email from Lambda using Amazon SES')
    }