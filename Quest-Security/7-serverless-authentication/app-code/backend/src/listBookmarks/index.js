const {DynamoDBClient, ScanCommand} = require("@aws-sdk/client-dynamodb");
const client = new DynamoDBClient();

exports.handler = async message => {
  console.log(message);

  let params = {
    TableName: process.env.TABLE_NAME,
    Select: 'ALL_ATTRIBUTES'
  };

  console.log(`Getting all bookmarks from table ${process.env.TABLE_NAME}`);
  const command = new ScanCommand(params);
  let results =  await client.send(command);
  console.log(`Done: ${JSON.stringify(results)}`);

  return {
    statusCode: 200,
    headers: {"Access-Control-Allow-Origin": '*'},
    body: JSON.stringify(results.Items)
  };
}
