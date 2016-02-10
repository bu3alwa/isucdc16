<?php
$LDAPHost = "192.168.1.3";
$dn="CN=Users,DC=team5,DC=isucdc,DC=com";

$ldapUser = "apache2power@team5.isucdc.com";
$ldapUserPass = "apache2powerOPC";

$SearchField="sAMAccountName";


$SearchFor="David";

$ldapCNX = ldap_connect($LDAPHost) or 
die("Connect Failed");

ldap_bind($ldapCNX, $ldapUser, $ldapUserPass) or 
die("Bind Failed: ");

//error_reporting(E_ALL ^ E_NOTICE);


?>



