<!-- Build VPC networks on AWS -->
1. Create cloud VPC A,B,C,D in one region
2. Create onprem vpc E
3. Create cloud VPC F in another region
4. Connect 1 and 3 together using TGW
5. Create a Site to Site VPN to connect 2 to 1 and 3 
6. Create VPC flow logs for any of the above for VPC CIDR, Subnet OR ENI 
7. pvc flow logs and athena integration

<!-- Security OF Networks, Users, and roles-->

<!-- Application deploment + DevOps + Monitoring-->

<!-- DNS and Route53 -->

<!-- IAC uisng CloudFormation, Ansible, and Terraform -->

<!-- Read more on howw to use AWS Network Firewall to restrict egress traffic in VPC -->
<!-- See samples here: https://github.com/aws-samples/aws-networkfirewall-cfn-templates -->
<!-- https://docs.aws.amazon.com/network-firewall/latest/developerguide/setting-up.html -->
<!-- Add solution for traffic mirroring -->
- So far this is what I glean from quest games
- Create a firewall (provides you an one endpoint for each subnet associated with the firewall)
- create a a network firewall rule group
- attach a rule group to a firewall policy
- use the endpoints to control traffic from one vpc/subnet to the other. To have your network traffic inspected by Network Firewall, you must direct traffic to firewall endpoints by using VPC route tables.
