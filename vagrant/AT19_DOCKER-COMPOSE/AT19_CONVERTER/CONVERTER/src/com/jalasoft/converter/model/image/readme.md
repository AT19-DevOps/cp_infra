##Important Notes! About PDF to image
___
Copyright Policy managed by "Imagemagick" prevents from manipulating PDF files in Ubuntu 22.04.1 LTS - Linux.

Considering the Legal implications with copyrights, the lines below describes a workaround to solve this limitation.

JALASOFT UNIVERSITY AND JALASOFT STUDENTS ARE NOT RESPONSABLE FOR ANY ILEGAL MANIPULATION OF COPYRIGHTED FILES. THIS WORKAROUND HAS ONLY EDUCATIONAL PURPOUSE.

1. Edit the file "policy.xml" with administrative rights.
    - `$ sudo nano /etc/ImageMagick-6/policy.xml`

2. Locate the line containig PDF atributes
    - "<policy domain="coder" rights="none" pattern="EPS" />"

3. Replace >'rights="none"' with
    - >rights="read | write"

4. Save and Exit  file. Enjoy!