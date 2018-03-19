from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

print "\n\n### ex 8 print crypto children ###"
for i in crypto:
  for child in i.children:
    print child.text

group2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

print "\n\n### ex 9 print group 2 ###" 
for i in group2:
  print i.text

non_aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec="set transform-set AES")

print "\n\n### ex 10 - not using AES"
for i in non_aes:
  print i.text
  for trans in i.children:
    if trans.text[:18] == " set transform-set":
      print trans.text[18:]
