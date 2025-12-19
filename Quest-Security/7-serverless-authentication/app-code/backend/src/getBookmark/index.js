const {DynamoDBClient, GetItemCommand} = require("@aws-sdk/client-dynamodb");
const client = new DynamoDBClient();

exports.handler = async message => {
  console.log(message);
  let bookmarkId = message.pathParameters.id
  let params = {
    TableName: process.env.TABLE_NAME,
    Key: {
      id: { S: bookmarkId }
    }
  };

  console.log(`Getting bookmark ${bookmarkId} from table ${process.env.TABLE_NAME}`);
  const command = new GetItemCommand(params);
  let results = await client.send(command);
  console.log(`Done: ${JSON.stringify(results)}`);

  return {
    statusCode: 200,
    headers: {"Access-Control-Allow-Origin": '*'},
    body: JSON.stringify(results.Item)
  };
}
