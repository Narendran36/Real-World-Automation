#!/usr/bin/env python3

import datetime
import os

from reports import generate_report
from emails import generate_email, send_email
student-00-141debd56499@linux-instance:~$ cat reports.py
#!/usr/bin/env python3

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate

def generate_report(file, title, add_info):
        styles = getSampleStyleSheet()
        report = SimpleDocTemplate(file)
        report_title = Paragraph(title, styles['h1'])
        report_info = Paragraph(add_info, styles['BodyText'])
        empty_line = Spacer(1,20)

        report.build([report_title, empty_line, report_info, empty_line])
