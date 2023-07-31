from transformers import pipeline
question_answerer = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

context = r"""
From: Mary Bryson <M.Bryson@navajo.com>
To: ['Yeini Martinez <Y.Martinez@navajo.com>']
Subject: FW: New ProTrans Load: L11498510
Body: b'PRO# 3031698\r\n\r\nFrom: noreply@protrans.com &lt;noreply@protrans.com&gt;\r\nSent: Sunday, July 23, 2023 6:02 AM\r\nTo: Expedited &lt;expedited@navajo.com&gt;; Joseph Kerr &lt;J.Kerr@navajo.com&gt;\r\nCc: loadtenders@protrans.com\r\nSubject: New ProTrans Load: L11498510\r\n\r\n[https://protrans.com/wp-content/uploads/2020/12/cropped-Protrans_Final_Logo.png]\r\nLOAD: L11498510   New   CARRIER\r\nPlan Name:elcav3\r\nMode:Truckload\r\nEquip Type:Dry Van 53 FT ,Service Level:Standard / Solo\r\n        Navajo Express NAVE\r\n1400 W. 64th Ave\r\nDenver, CO 80221 US\r\n\r\n\r\nRate Information: 1091.58 (USD) All IN Rate\r\nTender Response Time: 7/23/2023 05:02 MT\r\nCheck Call Requirements: Interval -None; Stop Dep;\r\n\r\nSTOP DETAILS\r\n  ________________________________\r\nSTOP 1\r\n   Window Start: 8/6/2023 16:00:00 MT\r\n   Window End: 8/6/2023 18:00:00 MT\r\n   Location: ProTrans El Paso\r\n                    12425 Rojas Street\r\n                    El Paso, TX 79928 US\r\n   Load Type: Live\r\n\r\n  ________________________________\r\nSTOP 2\r\n   Window Start: 8/7/2023 09:00:00 PT\r\n   Window End: 8/7/2023 10:00:00 PT\r\n   Location: ProTrans Calexico\r\n                    291 E. Campillo Ave Suite A\r\n                    Calexico, CA 92231 US\r\n   Load Type: Live\r\n\r\n  ________________________________\r\nMail Invoice To:        For the Account Of:\r\nProTrans International\r\nP.O. Box 42069\r\nIndianapolis, IN, 46241 US\r\n1 (317) 240-4100\r\n\r\n\r\n, ,\r\n\r\n\r\nCLICK THIS LINK TO ACCEPT OR REJECT LOAD REQUEST<https://u28958428.ct.sendgrid.net/ls/click?upn=p6pbgs04-2BLJs3DIHkDgJMwyr5Ve0IUw-2F23qzFfZxy8HIBIZ-2FRK57lEa6di4RWKYisjlWKKUDluj-2BMXRF-2FU9tRg-3D-3DkW1r_ccFvNIhX2vif9V3vfOeATkafpzffiLPZGIcVHkSQ7ktURMyeMzY5E7Vgo9Gu2-2B7U8a-2F2ZuTZvo6-2BpIsk9vASKa6ncz-2B9nVU-2B14KF8wWZ9RYE4gpjanutjGcIgnrP19Jy8MaMaKGFzYp3CnvtrJMN04kcyW7RStV1xjiTsyhFU8v5Sda-2FPsGP5Ioz2eKSRNDNjAejH34oFSNjDiXQaQmxAw-3D-3D>\r\nNote: Trouble viewing this request? Please view on carrier portal via the link above.\r\n\r\nThis is an auto-generated message. Please do not reply to this message.\r\n'
Attachments:
"""

result = question_answerer(question="What is the Location",     context=context)
print(result)
# print(
#     f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}"
