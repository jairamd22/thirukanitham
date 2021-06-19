# coding=utf8
 
import sys
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import uic
import datetime
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
import horoscope as hora
import math
from PyQt5 import QtGui as gui
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor, QBrush, QPainter
from dateutil.relativedelta import relativedelta
from PyQt5 import QtGui as qtg
from array import *
from PyQt5 import QtPrintSupport as qtps
from PyQt5.QtWebEngineWidgets import *

MW_Ui, MW_Base = uic.loadUiType('ep_v1.ui')

lineList = [line.rstrip('\n') for line in open('citynames.txt')]
geo_lat = [line.rstrip('\n') for line in open('geo_lat.txt')]
geo_lng = [line.rstrip('\n') for line in open('geo_lng.txt')]
#country = [line.rstrip('\n') for line in open('country.txt')]        
#province = [line.rstrip('\n') for line in open('province.txt')]
gmtoffset = [line.rstrip('\n') for line in open('gmtoffset.txt')]


timezones = [
        "Select Time Zone",
        "GMT -12:00 hrs - IDLW",
        "GMT -11:00 hrs - BET",
        "GMT -10:30 hrs - HST",
        "GMT -10:00 hrs - AHST",
        "GMT -09:30 hrs - HDT",
        "GMT -09:00 hrs - YST",
        "GMT -08:00 hrs - PST",
        "GMT -07:00 hrs - MST",
        "GMT -06:00 hrs - CST",
        "GMT -05:00 hrs - EST",
        "GMT -04:00 hrs - AST",
        "GMT -03:30 hrs - NST",
        "GMT -03:00 hrs - BZT2",
        "GMT -02:00 hrs - AT",
        "GMT -01:00 hrs - WAT",
        "Greenwich Mean Time - GMT",
        "GMT +01:00 hrs - CET",
        "GMT +02:00 hrs - EET",
        "GMT +03:00 hrs - BAT",
        "GMT +03:30 hrs - IT",
        "GMT +04:00 hrs - USZ3",
        "GMT +05:00 hrs - USZ4",
        "GMT +05:30 hrs - IST",
        "GMT +06:00 hrs - USZ5",
        "GMT +06:30 hrs - NST",
        "GMT +07:00 hrs - SST",
        "GMT +07:30 hrs - JT",
        "GMT +08:00 hrs - AWST",
        "GMT +08:30 hrs - MT",
        "GMT +09:00 hrs - JST",
        "GMT +09:30 hrs - ACST",
        "GMT +10:00 hrs - AEST",
        "GMT +10:30 hrs - ACDT",
        "GMT +11:00 hrs - UZ10",
        "GMT +11:30 hrs - NZ",
        "GMT +12:00 hrs - NZT",
        "GMT +12:30 hrs - NZS",
        "GMT +13:00 hrs - NZST"
]

timezonesvalues = [
        "0",
        "-12",
        "-11",
        "-10.5",
        "-10",
        "-9.5",
        "-9",
        "-8",
        "-7",
        "-6",
        "-5",
        "-4",
        "-3.5",
        "-3",
        "-2",
        "-1",
        "0",
        "1",
        "2",
        "3",
        "3.5",
        "4.5",
        "5",
        "5.5",
        "6",
        "6.5",
        "7",
        "07.5",
        "8",
        "8.5",
        "9",
        "9.5",
        "10",
        "10.5",
        "11",
        "11.5",
        "12",
        "12.5",
        "13"
]

rasivalues_global=[]
amsamvalues_global=[]
print_essentials=[]


class AnotherWindow(QWidget):

    def __init__(self, url='https://exactpredictions.in/',title='Exact Predictions'):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)      
        qurl = QUrl(url) 
        self.browser = QWebEngineView() 
        self.browser.setUrl(qurl)         
        layout.addWidget(self.browser)
        self.setWindowTitle(title)
        self.setWindowIcon(qtg.QIcon('favicon.ico')) 
        
class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0),language='english'):
        super().__init__()
     
        if language=="english":
            fnt = QFont('Courier New', font_size)
        
        if language=="tamil":
            fnt = QFont('Catamaran', font_size)
        
        fnt.setBold(set_bold)
 
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

class InvoiceView(qtw.QTextEdit):

    dpi = 300
    doc_width = 8.5 * dpi
    doc_height = 11 * dpi

    def __init__(self):
        super().__init__(readOnly=True)
        self.setFixedSize(qtc.QSize(self.doc_width, self.doc_height))


    def set_page_size(self, qrect):
        self.doc_width = qrect.width()
        self.doc_height = qrect.height()
        self.setFixedSize(qtc.QSize(self.doc_width, self.doc_height))
        self.document().setPageSize(
            qtc.QSizeF(self.doc_width, self.doc_height))

    def build_invoice(self, data):
        document = qtg.QTextDocument()
        self.setDocument(document)
        document.setPageSize(qtc.QSizeF(self.doc_width, self.doc_height))
        cursor = qtg.QTextCursor(document)
        root = document.rootFrame()
        cursor.setPosition(root.lastPosition())

        # Insert top-level frames
        logo_frame_fmt = qtg.QTextFrameFormat()
        logo_frame_fmt.setBorder(2)
        logo_frame_fmt.setPadding(10)
        logo_frame = cursor.insertFrame(logo_frame_fmt)

        cursor.setPosition(root.lastPosition())
        cust_addr_frame_fmt = qtg.QTextFrameFormat()
        cust_addr_frame_fmt.setWidth(self.doc_width * .3)
        cust_addr_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatRight)
        cust_addr_frame = cursor.insertFrame(cust_addr_frame_fmt)

        cursor.setPosition(root.lastPosition())
        terms_frame_fmt = qtg.QTextFrameFormat()
        terms_frame_fmt.setWidth(self.doc_width * .5)
        terms_frame_fmt.setPosition(qtg.QTextFrameFormat.FloatLeft)
        terms_frame = cursor.insertFrame(terms_frame_fmt)

        cursor.setPosition(root.lastPosition())
        line_items_frame_fmt = qtg.QTextFrameFormat()
        line_items_frame_fmt.setMargin(25)
        line_items_frame = cursor.insertFrame(line_items_frame_fmt)

        # Create the heading
        # create a format for the characters
        std_format = qtg.QTextCharFormat()

        logo_format = qtg.QTextCharFormat()
        logo_format.setFont(
            qtg.QFont('Impact', 24, qtg.QFont.DemiBold))
        logo_format.setUnderlineStyle(
            qtg.QTextCharFormat.SingleUnderline)
        logo_format.setVerticalAlignment(
            qtg.QTextCharFormat.AlignMiddle)

        label_format = qtg.QTextCharFormat()
        label_format.setFont(qtg.QFont('Sans', 12, qtg.QFont.Bold))

        # create a format for the block
        cursor.setPosition(logo_frame.firstPosition())
        # The easy way:
        #cursor.insertImage('nc_logo.png')
        # The better way:
        logo_image_fmt = qtg.QTextImageFormat()
        logo_image_fmt.setName('nc_logo.png')
        logo_image_fmt.setHeight(48)
        cursor.insertImage(logo_image_fmt, qtg.QTextFrameFormat.FloatLeft)
        cursor.insertText('   ')
        cursor.insertText('Ninja Coders, LLC', logo_format)
        cursor.insertBlock()
        cursor.insertText('123 N Wizard St, Yonkers, NY 10701', std_format)

        ## Customer address
        cursor.setPosition(cust_addr_frame.lastPosition())

        address_format = qtg.QTextBlockFormat()
        address_format.setLineHeight(
            150, qtg.QTextBlockFormat.ProportionalHeight)
        address_format.setAlignment(qtc.Qt.AlignRight)
        address_format.setRightMargin(25)

        cursor.insertBlock(address_format)
        cursor.insertText('Customer:', label_format)
        cursor.insertBlock(address_format)
        cursor.insertText(data['c_name'], std_format)
        cursor.insertBlock(address_format)
        cursor.insertText(data['c_addr'])

        ## Terms
        cursor.setPosition(terms_frame.lastPosition())
        cursor.insertText('Terms:', label_format)
        cursor.insertList(qtg.QTextListFormat.ListDisc)
        # cursor is now in the first list item

        term_items = (
            f'<b>Invoice dated:</b> {data["i_date"]}',
            f'<b>Invoice terms:</b> {data["i_terms"]}',
            f'<b>Invoice due:</b> {data["i_due"]}',
        )

        for i, item in enumerate(term_items):
            if i > 0:
                cursor.insertBlock()
            # We can insert HTML too, but not with a textformat
            cursor.insertHtml(item)

        ## Line items
        table_format = qtg.QTextTableFormat()
        table_format.setHeaderRowCount(1)
        table_format.setWidth(
            qtg.QTextLength(qtg.QTextLength.PercentageLength, 100))

        headings = ('Job', 'Rate', 'Hours', 'Cost')
        num_rows = len(data['line_items']) + 1
        num_cols = len(headings)

        cursor.setPosition(line_items_frame.lastPosition())
        table = cursor.insertTable(num_rows, num_cols, table_format)

        # now we're in the first cell of the table
        # write headers
        for heading in headings:
            cursor.insertText(heading, label_format)
            cursor.movePosition(qtg.QTextCursor.NextCell)

        # write data
        for row in data['line_items']:
            for col, value in enumerate(row):
                text = f'${value}' if col in (1, 3) else f'{value}'
                cursor.insertText(text, std_format)
                cursor.movePosition(qtg.QTextCursor.NextCell)

        # Append a row
        table.appendRows(1)
        cursor = table.cellAt(num_rows, 0).lastCursorPosition()
        cursor.insertText('Total', label_format)
        cursor = table.cellAt(num_rows, 3).lastCursorPosition()
        cursor.insertText(f"${data['total_due']}", label_format)
        
    def build_horoscope(self,language, data, data_amsam, planettable_html, print_essentials):
        document = qtg.QTextDocument()
        self.setDocument(document)
        document.setPageSize(qtc.QSizeF(self.doc_width, self.doc_height))
        document.setDocumentMargin(25)  
        document.setTextWidth(self.doc_width)
        cursor = qtg.QTextCursor(document)
        root = document.rootFrame()

        # Must come before the HTML is inserted
        document.setDefaultStyleSheet(
            'body {color: #000; font-size: 10px;  margin-left: 10; margin-right: 10;} '
            'h3 {font-family: "Catamaran"; color: black; font-size: 2pt; text-align: left;} '
            'h2 {font-family: "Catamaran"; color: black; font-size: 9px; text-align: center;} '
            'h1 {background: black; color: white; font-size: 12px; text-align: center;} '
            'table, td, th { border: 1px solid black;}'
            'table { width: 100%;border-collapse: collapse;}'
            'table { font-family: "Catamaran"; font-size: 12px;}'
            #'td, th { margin-top: 3; margin-left: 3; margin-right: 3; margin-bottom: 3;}'
            'td, th { padding-top: 1; padding-left: 5; padding-right: 5; padding-bottom: 1; align: right; }'
            'th { font-family: "Catamaran"; color: black; font-size: 12px; }'
            '.class_head1 { font-family: "Catamaran"; font-size: 12px; text-align: center; }'
            '.class_head2 { font-family: "Arial"; font-size: 12px; text-align: right; }'
            )
                
        
        if language=="english":
            head1 = "Thirumagal Jotida Nilayam"
            head2 = "Astrologer 'Guru' Bakkianathan 1378, 19th East Cross Street"
            head3 = "MKB Nagar, Chennai-39. Ph: 9840324409"
            rasi_lbl = "Rasi "
            navamsam_lbl = "Navamsam"  
            footertext = "Thirukanitham. Chitra Paksha Ayanamsa Method Used<br>&#169; www.exactpredictions.in | 9840324409"
            
            #panjangam_html = "<table><tr><td colspan=7><h2>"+ print_essentials[0] +"</h2></td></tr><tr><th width='14%'>Lagna</th><th width='13%'>Rasi</th><th width='17%'>Star</th><th width='14%'>Thithi</th><th width='14%'>Karna</th><th width='14%'>Yoga</th><th width='16%'>Day</th></tr><tr><td>" +  print_essentials[5] + "</td><td>" + print_essentials[6] + "</td><td>" + print_essentials[7] + "</td><td>" + print_essentials[8] + "</td><td>" + print_essentials[9] + "</td><td>" + print_essentials[10] + "</td><td>" + print_essentials[11] + "</td></tr></table>"     

            panjangam_html = "<table width='100%'><tr><td width='20%'>Name</td><td width='30%'>" + print_essentials[0] +"</td><td width='20%'>Lagna</td><td width='30%'>" + print_essentials[5] +"</td></tr><tr><td width='20%'>Gender </td><td width='30%'>" + print_essentials[1] +"</td><td width='20%'>Rasi</td><td width='30%'>" + print_essentials[6] +"</td></tr><tr><td width='20%'>Birth Date </td><td width='30%'>" + print_essentials[2] +"</td><td width='20%'>Star</td><td width='30%'>" + print_essentials[7] +"</td></tr><tr><td width='20%'>Birth Time</td><td width='30%'>" + print_essentials[3] +"</td><td width='20%'>Thithi</td><td width='30%'>" + print_essentials[8] +"</td></tr><tr><td width='20%'>Birth Place</td><td width='30%'>" + print_essentials[4] +"</td><td width='20%'>Karna</td><td width='30%'>" + print_essentials[9] +"</td></tr><tr><td width='20%'>Name Letters</td><td width='30%'>" + print_essentials[13] +"</td><td width='20%'>யோகம்</td><td width='30%'>" + print_essentials[10] +"</td></tr><tr><td width='20%'>Star Tree</td><td width='30%'>" + print_essentials[14] +"</td><td width='20%'>Day</td><td width='30%'>" + print_essentials[11] +"</td></tr></table>"
            
        elif language=="tamil":
            head1 = "திருமகள் ஜோதிட நிலையம் "
            head2 = "1378, 19th East Cross Street, MKB Nagar,"
            head3 = "Jothidar. Bakkia Nathan, 98432 4409"
            rasi_lbl = "ராசி"
            navamsam_lbl = "நவாம்சம்"       
            
            footertext = "திருக்கணிதம். சித்ர பக்ஷ அயனாம்சம் முறைப்படி கணிக்கப்பட்டது <br>&#169; www.exactpredictions.in | 9840324409"
            
            #panjangam_html = "<table><tr><td colspan=7><h2>"+ print_essentials[0] +"</h2></td></tr><tr><th width='13%'>லக்கினம்</th><th width='13%'>ராசி</th><th width='18%'>நட்சத்திரம்</th><th width='14%'>திதி</th><th width='14%'>கர்ணம்</th><th width='14%'>யோகம்</th><th width='16%'>கிழமை </th></tr><tr><td>" +  print_essentials[5] + "</td><td>" + print_essentials[6] + "</td><td>" + print_essentials[7] + "</td><td>" + print_essentials[8] + "</td><td>" + print_essentials[9] + "</td><td>" + print_essentials[10] + "</td><td>" + print_essentials[11] + "</td></tr></table>"
            
            panjangam_html = "<table width='100%'><tr><td width='20%'>பெயர்</td><td width='30%'>" + print_essentials[0] +"</td><td width='20%'>லக்கினம்</td><td>" + print_essentials[5] +"</td></tr><tr><td width='20%'>பாலினம் </td><td width='30%'>" + print_essentials[1] +"</td><td width='20%'>ராசி</td><td width='30%'>" + print_essentials[6] +"</td></tr><tr><td width='20%'>பிறந்த தேதி </td><td width='30%'>" + print_essentials[2] +"</td><td>நட்சத்திரம்</td><td width='30%'>" + print_essentials[7] +"</td></tr><tr><td width='20%'>பிறந்த நேரம் </td><td width='30%'>" + print_essentials[3] +"</td><td width='20%'>திதி</td><td width='30%'>" + print_essentials[8] +"</td></tr><tr><td width='20%'>பிறந்த இடம்</td><td width='30%'>" + print_essentials[4] +"</td><td width='20%'>கர்ணம்</td><td width='30%'>" + print_essentials[9] +"</td></tr><tr><td width='20%'>பெயர் எழுத்து</td><td width='30%'>" + print_essentials[13] +"</td><td width='20%'>யோகம்</td><td width='30%'>" + print_essentials[10] +"</td></tr><tr><td width='20%'>நட்சத்திர மரம் </td><td width='30%'>" + print_essentials[14] +"</td><td width='20%'>கிழமை</td><td width='30%'>" + print_essentials[11] +"</td></tr></table>"
            
            
        # Create the heading
        # create a format for the characters

        std_format = qtg.QTextCharFormat()

        tam_head = qtg.QTextCharFormat()
        tam_head.setFont(
            qtg.QFont('Catamaran', 14, qtg.QFont.Bold))
        tam_head.setVerticalAlignment(
            qtg.QTextCharFormat.AlignMiddle)      

        tam_head1 = qtg.QTextCharFormat()
        tam_head1.setFont(
            qtg.QFont('Catamaran', 11, qtg.QFont.Bold))
        tam_head1.setVerticalAlignment(
            qtg.QTextCharFormat.AlignMiddle)              
        
        tam_format = qtg.QTextCharFormat()
        tam_format.setFont(
            qtg.QFont('Catamaran', 9, qtg.QFont.Normal))
        tam_format.setVerticalAlignment(
            qtg.QTextCharFormat.AlignMiddle)
            
        label_format = qtg.QTextCharFormat()
        label_format.setFont(qtg.QFont('Sans', 9))
        label_format.setVerticalAlignment(
            qtg.QTextCharFormat.AlignMiddle)

        line_items_frame_fmt = qtg.QTextFrameFormat()
        line_items_frame_fmt.setBorder(0)
        line_items_frame_fmt.setBorderStyle(0)
        line_items_frame_fmt.setMargin(7)        

        
        #cursor.setPosition(root.lastPosition())
        #logo_frame_fmt = qtg.QTextFrameFormat()
        #logo_frame_fmt.setBorder(0)
        #logo_frame_fmt.setBorderStyle(0)
        #logo_frame_fmt.setMargin(5)        
        #logo_frame = cursor.insertFrame(logo_frame_fmt)
        
        #cursor.insertText(print_essentials[0], tam_head)
        #cursor.insertBlock()
        #cursor.insertText(head2, tam_format)
        #cursor.insertBlock()
        #cursor.insertText(head3, tam_format)
        
        table_format1 = qtg.QTextTableFormat()
        table_format1.setBorder(0)
        table_format1.setBorderStyle(0)
        table_format1.setMargin(0)
        table_format1.setCellSpacing(0)
        table_format1.setWidth(
            qtg.QTextLength(qtg.QTextLength.PercentageLength, 100))

        table_format2 = qtg.QTextTableFormat()
        table_format2.setBorder(1)
        table_format2.setBorderBrush(Qt.black)
        table_format2.setAlignment(Qt.AlignHCenter)
        table_format2.setBorderStyle(3)
        table_format2.setMargin(7)
        table_format2.setPadding(0)
        table_format2.setCellSpacing(0)
        table_format2.setCellPadding(3)
        table_format2.setWidth(
            qtg.QTextLength(qtg.QTextLength.PercentageLength, 100))
            
        table_format2.setAlignment(Qt.AlignCenter)
            

        constraints = [gui.QTextLength(gui.QTextLength.PercentageLength, 25),
                   gui.QTextLength(gui.QTextLength.PercentageLength, 25),
                   gui.QTextLength(gui.QTextLength.PercentageLength, 25),
                   gui.QTextLength(gui.QTextLength.PercentageLength, 25)]        

        panjangam_constraints = [gui.QTextLength(gui.QTextLength.PercentageLength, 20),
                   gui.QTextLength(gui.QTextLength.PercentageLength, 20),
                   gui.QTextLength(gui.QTextLength.PercentageLength, 20),
                   gui.QTextLength(gui.QTextLength.PercentageLength, 20),
                   gui.QTextLength(gui.QTextLength.PercentageLength, 20)]
                   
        cursor.setPosition(root.lastPosition())
        panjangam_frame = cursor.insertFrame(line_items_frame_fmt)


        cursor.insertHtml(panjangam_html)
        
        table_format2.setColumnWidthConstraints(constraints)
        
        cursor.setPosition(root.lastPosition())
        table = cursor.insertTable(1, 2, table_format1)        
        table1 = cursor.insertTable(4, 4, table_format2) 
        table1.mergeCells(1,1,2,2);
        

        cursor.insertText(data[11],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)        
        cursor.insertText(data[0],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[1],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[2],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[10],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(rasi_lbl,tam_head1)
        cursor.insertBlock()
        cursor.insertText(print_essentials[2],tam_format)
        cursor.insertBlock()
        cursor.insertText(print_essentials[3],tam_format)  
        #cursor.insertBlock()
        #cursor.insertText(print_essentials[4],tam_format)           
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[3],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[9],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[4],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[8],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[7],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[6],tam_format)            
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data[5],tam_format)

        
        
        cursor.setPosition(table.lastPosition())    
        table2 = cursor.insertTable(4, 4, table_format2) 
        table2.mergeCells(1,1,2,2);
        
        
        cursor.insertText(data_amsam[11],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)        
        cursor.insertText(data_amsam[0],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[1],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[2],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[10],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(navamsam_lbl,tam_head1)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[3],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[9],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[4],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[8],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[7],tam_format)
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[6],tam_format)            
        cursor.movePosition(qtg.QTextCursor.NextCell)    
        cursor.insertText(data_amsam[5],tam_format)        
        
        cursor.setPosition(root.lastPosition())
            
        dasa_frame = cursor.insertFrame(line_items_frame_fmt) 
        cursor.insertHtml(print_essentials[12])
        
        cursor.setPosition(root.lastPosition())

        line_items_frame = cursor.insertFrame(line_items_frame_fmt)    
        
        cursor.insertHtml(planettable_html)
        
        #cursor.setPosition(root.lastPosition())
        
        #foot_frame = cursor.insertFrame(line_items_frame_fmt) 
        
        cursor.insertHtml(footertext)
       
                
                
#class MainWindow(qtw.QWidget, Ui_MainWindow):
class MainWindow(MW_Base, MW_Ui):
    events = {}

    
    def __init__(self):
        """MainWindow constructor. """
        super().__init__()
        self.setupUi(self)
        
        #self.lineEdit_Nativename.setText("Transit")
        self.cleenlabels()
                      
        dt = QDate.currentDate()
        ti = QTime.currentTime()
        
        self.dateEdit_Dob.setDisplayFormat("dd-MM-yyyy") 
        self.dateEdit_Dob.setDate(dt) 
        self.timeEdit_Btime.setTime(ti) 
        
        self.onlyInt = gui.QIntValidator()
        self.onlyDouble = gui.QDoubleValidator()
        
        self.lineEdit_Longitudedeg.setValidator(self.onlyInt)
        self.lineEdit_Longitudemin.setValidator(self.onlyDouble)
        self.lineEdit_Lattitudedeg.setValidator(self.onlyInt)
        self.lineEdit_Lattitudemin.setValidator(self.onlyDouble)


        completer = QCompleter(lineList)
        self.lineEdit_Birthplace.setCompleter(completer)
        self.lineEdit_Birthplace.editingFinished.connect(self.placeentered)
        self.lineEdit_Birthplace.textChanged.connect(self.placeentered)
        self.lineEdit_Birthplace.textEdited.connect(self.to_upper)

        self.actionExit.triggered.connect(self.closethirumaglapp)
        self.actionNew.triggered.connect(self.newHoro)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionExport_PDF.triggered.connect(self.export_pdf)
        self.actionConfigure_Printer.triggered.connect(self.printer_config)
        self.actionPrint_Preview.triggered.connect(self.print_preview)
        self.actionPrint_Dialog.triggered.connect(self.print_dialog)
        self.actionExact_Predictions.triggered.connect(self.show_website)
        self.actionGuru_Bakkianathan.triggered.connect(self.show_gurubakkianathan)
        self.actionAbout_Exact_Predictions.triggered.connect(self.aboutep)
        
        self.toolButton_Placesearch.clicked.connect(self.citylatlong)
        
        self.pushButton_mainreport.clicked.connect(self.show_horoscope)
        
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow("https://exactpredictions.in/gurubakkianathan/","Guru Bakkianathan")
        
        self.lineEdit_Birthplace.setText("CHENNAI - TAMIL NADU - INDIA")

        self.pushButton_conf.clicked.connect(self.printer_config)
        self.pushButton_preview.clicked.connect(self.print_preview)
        self.pushButton_print.clicked.connect(self.print_dialog)
        self.pushButton_pdf.clicked.connect(self.export_pdf)
           
        self.preview = InvoiceView()
        self.verticalLayout_5.addWidget(self.preview)
             

        # Printing
        #print_tb = self.addToolBar('Printing')
        #print_tb.addAction('Configure Printer', self.printer_config)
        #print_tb.addAction('Print Preview', self.print_preview)
        #print_tb.addAction('Print dialog', self.print_dialog)
        #print_tb.addAction('Export PDF', self.export_pdf)

        self.printer = qtps.QPrinter()
        # Configure defaults:
        self.printer.setOrientation(qtps.QPrinter.Portrait)
        self.printer.setPageSize(qtg.QPageSize(qtg.QPageSize.Letter))
        self._update_preview_size()

    
        self.showMaximized()
        self.show()
        self.show_horoscope()

        
    def _update_preview_size(self):
        self.preview.set_page_size(
            self.printer.pageRect(qtps.QPrinter.Point))

    def printer_config(self):
        dialog = qtps.QPageSetupDialog(self.printer, self)
        dialog.exec()
        self._update_preview_size()

    def _print_document(self):
        # doesn't actually kick off printer,
        # just paints document to the printer object
        self.preview.document().print(self.printer)

    def print_dialog(self):
        # Errata:  the book contained this line:
        #self._print_document()
        # As noted by DevinLand in issue #8, this can cause the document to start printing.
        dialog = qtps.QPrintDialog(self.printer, self)

        # Instead we'll add this line, so _print_document is triggered when the dialog is
        # accepted:
        dialog.accepted.connect(self._print_document)
        dialog.exec()
        self._update_preview_size()

    def print_preview(self):
        dialog = qtps.QPrintPreviewDialog(self.printer, self)
        dialog.paintRequested.connect(self._print_document)
        dialog.exec()
        self._update_preview_size()

    def export_pdf(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self, "Save to PDF", qtc.QDir.homePath(), "PDF Files (*.pdf)")
        if filename:
            self.printer.setOutputFileName(filename)
            self.printer.setOutputFormat(qtps.QPrinter.PdfFormat)
            self._print_document()

    def newHoro(self):
        self.cleenlabels()
                      
        dt = QDate.currentDate()
        ti = QTime.currentTime()
        
        self.dateEdit_Dob.setDisplayFormat("dd-MM-yyyy") 
        self.dateEdit_Dob.setDate(dt) 
        
        self.timeEdit_Btime.setDisplayFormat("HH:mm") 
        self.timeEdit_Btime.setTime(ti) 
        
        self.onlyInt = gui.QIntValidator()
        self.onlyDouble = gui.QDoubleValidator()
        
        self.lineEdit_Longitudedeg.setValidator(self.onlyInt)
        self.lineEdit_Longitudemin.setValidator(self.onlyDouble)
        self.lineEdit_Lattitudedeg.setValidator(self.onlyInt)
        self.lineEdit_Lattitudemin.setValidator(self.onlyDouble)


        completer = QCompleter(lineList)
        self.lineEdit_Birthplace.setCompleter(completer)
        self.lineEdit_Birthplace.editingFinished.connect(self.placeentered)
        self.lineEdit_Birthplace.textChanged.connect(self.placeentered)
        self.lineEdit_Birthplace.textEdited.connect(self.to_upper)
        self.lineEdit_Birthplace.setText("CHENNAI - TAMIL NADU - INDIA")
        self.lineEdit_Nativename.setText("")        
        self.comboBox_Sex.setCurrentIndex(0)  
        self.comboBox_Language.setCurrentIndex(0) 
        self.show_horoscope()
                
    def show_website(self):
        self.window1.showMaximized()
        self.window1.show() 
        
    def show_gurubakkianathan(self):
        self.window2.showMaximized()
        self.window2.show() 
    
    def aboutep(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Exact Predictions Desktop Applicaiton Beta Version 1.0\nAll Rights Reserved To Guru Bakkianathan, www.exactpredictions.in")
        msgBox.setWindowTitle("About")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(qtg.QIcon('favicon.ico')) 
        returnValue = msgBox.exec()

    def citylatlong(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Please type the city name in the behind box and select the city, Then the Lattitude, Longitude and Timezone details will be taken automattically.\n\nIf you not find any city in the list, do not worry, type the city name manually, also add timezone, Lattitude, Longitude details manually. You can find these information in google.\n\nIf you are in day/night saving country region, please select timezone manually hours before and after as per your region.")
        msgBox.setWindowTitle("About Place Selection")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(qtg.QIcon('favicon.ico')) 
        returnValue = msgBox.exec()
        
    def saveFile(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self,
            "Select the file to save to…",
            qtc.QDir.homePath(),
            'Horoscope Files (*.hor) ;; All Files (*)'
        )
        if filename:
            try:
                native_name = self.lineEdit_Nativename.text()
                native_sex = self.comboBox_Sex.currentText()
                native_date = self.dateEdit_Dob.date()
                native_time = self.timeEdit_Btime.time()
                native_day = native_date.day()
                native_month = native_date.month()
                native_year = native_date.year()
                native_hour = native_time.toString("hh")
                native_minutes = native_time.toString("mm")
                native_seconds = native_time.toString("ss")
                native_birthplace = self.lineEdit_Birthplace.text()
                native_timezone = self.comboBox_Timezone.currentText()
                native_longdeg = self.lineEdit_Longitudedeg.text()
                native_longdir = self.comboBox_Longitudedir.currentText()
                native_longmin = self.lineEdit_Longitudemin.text()
                native_latdeg = self.lineEdit_Lattitudedeg.text()
                native_latdir = self.comboBox_Lattitudedir.currentText()
                native_latmin = self.lineEdit_Lattitudemin.text()
                native_language = self.comboBox_Language.currentText()
                
                filehoro = str(native_name) + "\n" + str(native_sex) + "\n" + str(native_day) + "\n" + str(native_month) + "\n" + str(native_year) + "\n" + str(native_hour) + "\n" + str(native_minutes) + "\n" + str(native_seconds) + "\n" + str(native_birthplace) + "\n" + str(native_timezone) + "\n" + str(native_longdeg) + "\n" + str(native_longdir) + "\n" + str(native_longmin) + "\n" + str(native_latdeg) + "\n" + str(native_latdir) + "\n" + str(native_latmin) + "\n" + str(native_language)
                
                with open(filename, 'w') as fh:
                    fh.write(filehoro)
            except Exception as e:
                # Errata:  Book contains this line:
                #qtw.QMessageBox.critical(f"Could not save file: {e}")
                # It should read like this:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")            
            
    def openFile(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "Select a text file to open…",
            qtc.QDir.homePath(),
            'Horoscope Files (*.hor) ;; All Files (*)'
        )
        if filename:
            try:
                #with open(filename, 'r') as fh:
                #    filehoro = fh.read()
                
                filehoro = [filehoroline.rstrip('\n') for filehoroline in open(filename)]        
                print (filehoro)
                
                self.lineEdit_Nativename.setText(filehoro[0])
                
                if filehoro[1] == "Unknown":
                    self.comboBox_Sex.setCurrentIndex(0)  
                elif filehoro[1] == "Male":
                    self.comboBox_Sex.setCurrentIndex(1)  
                elif filehoro[1] == "Female":
                    self.comboBox_Sex.setCurrentIndex(2)                      
  
                d = QDate(int(filehoro[4]), int(filehoro[3]), int(filehoro[2])) 
                
                self.dateEdit_Dob.setDisplayFormat("dd-MM-yyyy") 
                self.dateEdit_Dob.setDate(d) 
                
                t = QTime(int(filehoro[5]), int(filehoro[6]), int(filehoro[7])) 
                self.timeEdit_Btime.setTime(t) 

                self.lineEdit_Birthplace.setText(filehoro[8])
                

                timezoneindex = timezones.index(filehoro[9])

                native_longdir = filehoro[11]
                native_latdir = filehoro[14]
                
                self.comboBox_Timezone.setCurrentIndex(timezoneindex)
                
                if native_longdir == "W":
                   self.comboBox_Longitudedir.setCurrentIndex(1)
                elif native_longdir == "E":
                   self.comboBox_Longitudedir.setCurrentIndex(0)
                
                if native_latdir == "N":
                   self.comboBox_Lattitudedir.setCurrentIndex(0)
                elif native_latdir == "S":
                   self.comboBox_Lattitudedir.setCurrentIndex(1)        
                   
                self.lineEdit_Longitudedeg.setText(filehoro[10])
                self.lineEdit_Longitudemin.setText(filehoro[12])
                self.lineEdit_Lattitudedeg.setText(filehoro[13])
                self.lineEdit_Lattitudemin.setText(filehoro[15])
                
                lang = filehoro[16]
                
                if lang == "Tamil":
                    self.comboBox_Language.setCurrentIndex(0)
                elif lang == "English":
                    self.comboBox_Language.setCurrentIndex(1)
        
                self.show_horoscope()
        
            except Exception as e:
                # Errata:  Book contains the following line:
                #qtw.QMessageBox.critical(f"Could not load file: {e}")
                # It should read like this:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")
                
    def closethirumaglapp(self):
        self.close()

    def to_upper(self, txt):
        self.lineEdit_Birthplace.setText(txt.upper())
    
    def show_horoscope(self):
        self.cleenlabels()
        native_name = self.lineEdit_Nativename.text()
        native_sex = self.comboBox_Sex.currentText()
        native_date = self.dateEdit_Dob.date()
        native_time = self.timeEdit_Btime.time()
        native_day = native_date.day()
        native_month = native_date.month()
        native_year = native_date.year()
        native_hour = native_time.toString("hh")
        native_minutes = native_time.toString("mm")
        native_seconds = native_time.toString("ss")
        native_birthplace = self.lineEdit_Birthplace.text()
        native_timezone = self.comboBox_Timezone.currentText()
        native_longdeg = self.lineEdit_Longitudedeg.text()
        native_longdir = self.comboBox_Longitudedir.currentText()
        native_longmin = self.lineEdit_Longitudemin.text()
        native_latdeg = self.lineEdit_Lattitudedeg.text()
        native_latdir = self.comboBox_Lattitudedir.currentText()
        native_latmin = self.lineEdit_Lattitudemin.text()
        native_language = self.comboBox_Language.currentText()
        tp_date = str(native_day) + "." + str(native_month) + "." + str(native_year)

        

        
        timezoneindex = timezones.index(native_timezone)
        native_timezone_value = timezonesvalues[timezoneindex]
        
        if native_longdir == "W":
           ew = -1
        elif native_longdir == "E":
           ew = 1
        
        if native_latdir == "N":
           ns = 1
        elif native_latdir == "S":
           ns = -1
        
        intz = float(native_timezone_value);

        my_longitude = ew * (int(native_longdeg) + (int(native_longmin) / 60));
        my_latitude = ns * (int(native_latdeg) + (int(native_latmin) / 60));

        if intz >= 0:
            whole = math.floor(intz)
            fraction = intz - math.floor(intz)
        else:
            whole = math.ceil(intz)
            fraction = intz - math.ceil(intz)

        inhours = int(native_hour) - whole
        inmins = int(native_minutes) - (fraction * 60)

        tp_time = str(inhours) + ":" + str(inmins)
        tp_longitude = str(my_longitude)
        tp_latitude = str(my_latitude)
        
        #print(tp_date)
        #print(tp_time)
        #print(tp_longitude)
        #print(tp_latitude)
        
        #print(native_longdir)        
        #print(native_timezone_value)
        #print(native_longdirvalue)
        #print(native_latdirvalue)
        
        #print(native_day)            
        #print(native_month)
        #print(native_year)
        #print(native_time)
        #print(native_hour)
        #print(native_minutes)
        #print(native_seconds)
        
        if native_language == "Tamil":
            self.label_panjangam.setText("")
            self.label_dasa.setText("")
            self.horoscope_tamil(tp_date, tp_time, tp_longitude, tp_latitude)
        elif native_language == "English":
            self.label_panjangam.setText("")
            self.label_dasa.setText("")
            self.horoscope(tp_date, tp_time, tp_longitude, tp_latitude)
            

    def cleenlabels(self):
        self.rasi_mesham_lbl.setText("")
        self.rasi_rishabam_lbl.setText("")
        self.rasi_mithunam_lbl.setText("")
        self.rasi_kadagam_lbl.setText("")
        self.rasi_simmam_lbl.setText("")
        self.rasi_kanni_lbl.setText("")
        self.rasi_thulam_lbl.setText("")
        self.rasi_viruchigam_lbl.setText("")
        self.rasi_dhanusu_lbl.setText("")
        self.rasi_magaram_lbl.setText("")
        self.rasi_kumbam_lbl.setText("")
        self.rasi_meenam_lbl.setText("")
        self.rasi_center_lbl.setText("RASI")
        
        self.amsam_mesham_lbl.setText("")
        self.amsam_rishabam_lbl.setText("")
        self.amsam_mithunam_lbl.setText("")
        self.amsam_kadagam_lbl.setText("")
        self.amsam_simmam_lbl.setText("")
        self.amsam_kanni_lbl.setText("")
        self.amsam_thulam_lbl.setText("")
        self.amsam_viruchigam_lbl.setText("")
        self.amsam_dhanusu_lbl.setText("")
        self.amsam_magaram_lbl.setText("")
        self.amsam_kumbam_lbl.setText("")
        self.amsam_meenam_lbl.setText("")
        self.amsam_center_lbl.setText("NAVAMSAM")


    def placeentered(self):
        native_birthplace = self.lineEdit_Birthplace.text()
        #cityindex = lineList.index(native_birthplace) 
        
        try:
            cityindex = lineList.index(native_birthplace) 
        except ValueError:
            cityindex = 0        
        
        
        tmp_gmtoffset = str(gmtoffset[cityindex])
        tmp_timezone_offset = timezonesvalues.index(tmp_gmtoffset)
        tmp_geo_lat = float(geo_lat[cityindex])
        tmp_geo_lang = float(geo_lng[cityindex])
        
        if tmp_geo_lat > 0:
            tmp_lat_dir = "N"
        else:
            tmp_lat_dir = "S"
            
        if tmp_geo_lang > 0:
            tmp_lang_dir = "E"
        else:
            tmp_lang_dir = "W"
        
        tmp_geo_lat = str(tmp_geo_lat)
        tmp_geo_lang = str(tmp_geo_lang)
        
        tmp_geo_lat_arr = tmp_geo_lat.split(".",1)   
        tmp_geo_lat_deg = tmp_geo_lat_arr[0]    
        tmp_geo_lat_min = tmp_geo_lat_arr[1]
        
        tmp_geo_lang_arr = tmp_geo_lang.split(".",1)   
        tmp_geo_lang_deg = tmp_geo_lang_arr[0]
        tmp_geo_lang_min = tmp_geo_lang_arr[1]
        
        #tmp_geo_lat_deg = math.trunc(tmp_geo_lat)
        #tmp_geo_lat_min = str(tmp_geo_lat)
        #tmp_geo_lat_min = tmp_geo_lat_min.split(".",1)
        
        #self.comboBox_Timezone.currentText()
        self.lineEdit_Longitudedeg.setText(str(tmp_geo_lang_deg))
        #self.comboBox_Longitudedir.currentText()
        self.lineEdit_Longitudemin.setText(str(tmp_geo_lang_min))
        self.lineEdit_Lattitudedeg.setText(str(tmp_geo_lat_deg))
        #self.comboBox_Lattitudedir.currentText()
        self.lineEdit_Lattitudemin.setText(str(tmp_geo_lat_min))
        
        tmp_timezone_val = timezones[tmp_timezone_offset]
        self.comboBox_Timezone.setCurrentText(tmp_timezone_val)

        self.comboBox_Longitudedir.setCurrentText(tmp_lang_dir)
        self.comboBox_Lattitudedir.setCurrentText(tmp_lat_dir)
        
        
        #print (native_birthplace)  
        #print (cityindex)  
        #print (tmp_timezone_offset)
        #print (tmp_gmtoffset)
        #print (tmp_timezone_val)

 
        
        
    def horoscope(self, p_date, p_time, p_longitude, p_latitude):
        #txtcmd = "swetest -edire: -b29.10.1977 -ut16:00 -p0123456789tm -house80.28333333,13.08333333,O -eswe -fPlLs -g, -n1 -s1 -sid1 -head"

        txtcmd = "swetest -edire: -b" + p_date + " -ut" + p_time + " -p0123456789tm -house" + p_longitude + "," + p_latitude + ",O -eswe -fPlLs -g, -n1 -s1 -sid1 -head"
        
        batcmd = txtcmd

        result_code = os.system(batcmd + ' > output.txt')
        if os.path.exists('output.txt'):
            fp = open('output.txt', "r")

        Lines = fp.readlines() 
  
        count = 0
        arr = []

        # Strips the newline character 
        for line in Lines: 
            arr.append(line.strip())

        lagnamtxt=""
        lagnamlat=""
        chandrantxt=""
        moonlat=""
        sooriyantxt=""
        sunlat=""
        bhudhantxt=""
        bhudhanlat=""
        bhudhanvakram=""
        sukrantxt=""
        sukranlat=""
        sukranvakram=""
        sevvaitxt=""
        sevvailat=""
        sevvaivakram=""
        gurutxt=""
        gurulat=""
        guruvakram=""
        sanitxt=""
        sanilat=""
        sanivakram=""
        raghutxt=""
        raghulat=""
        kethutxt=""
        kethulat=""
        lagnamhouse=""
        sunhouse=""
        moonhouse=""
        bhudhanhouse=""
        sukranhouse=""
        sevvaihouse=""
        guruhouse=""
        sanihouse=""
        raghuhouse=""
        kethuhouse=""

        rasimesham = []
        rasirishabam = []
        rasimithunam = []
        rasikadagam = []
        rasisimmam = []
        rasikanni = []
        rasithulam =  []
        rasiviruchigam = []
        rasidhanusu = []
        rasimagaram = []
        rasikumbam = []
        rasimeenam = []
    
        amsam_rasimesham = []
        amsam_rasirishabam = []
        amsam_rasimithunam = []
        amsam_rasikadagam = []
        amsam_rasisimmam = []
        amsam_rasikanni = []
        amsam_rasithulam =  []
        amsam_rasiviruchigam = []
        amsam_rasidhanusu = []
        amsam_rasimagaram = []
        amsam_rasikumbam = []
        amsam_rasimeenam = []
        
        for x in arr:
            planets = x.split(",");    
            cnt = len(planets)

            pl = planets[0].strip().upper();
            

                
            if pl == 'MOON':
                chandrantxt = "MOON"
                moonlat = planets[1].strip()
                moonhouse = hora.get_planet_house(float(moonlat))
                moon_amsamhouse = hora.amsamrasi(float(moonlat))                        
                moonhouse_english = hora.get_planet_house_english(float(moonlat))
                moondegree = hora.get_planet_degree(float(moonlat))    
                moonstar = hora.star_query_english(float(moonlat))   
            elif pl == 'SUN':
                sooriyantxt="SUN"
                sunlat = planets[1].strip()
                sunhouse = hora.get_planet_house(float(sunlat))    
                sun_amsamhouse = hora.amsamrasi(float(sunlat))                    
                sunhouse_english = hora.get_planet_house_english(float(sunlat))                
                sundegree = hora.get_planet_degree(float(sunlat))    
                sunstar = hora.star_query_english(float(sunlat))                  
            elif pl == 'MERCURY':
                bhudhanlat = planets[1].strip()
                bhudhanhouse = hora.get_planet_house(float(bhudhanlat))
                bhudhan_amsamhouse = hora.amsamrasi(float(bhudhanlat))                
                bhudhanhouse_english = hora.get_planet_house_english(float(bhudhanlat))            
                bhudhandegree = hora.get_planet_degree(float(bhudhanlat))
                bhudhanstar = hora.star_query_english(float(bhudhanlat))  
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        bhudhanvakram="TRUE";
                        bhudhantxt="Me(R)";
                    else:
                        bhudhanvakram="FALSE";
                        bhudhantxt="Me";
            elif pl == 'VENUS':
                sukranlat = planets[1].strip()
                sukranhouse = hora.get_planet_house(float(sukranlat))  
                sukran_amsamhouse = hora.amsamrasi(float(sukranlat))                
                sukranhouse_english = hora.get_planet_house_english(float(sukranlat))        
                sukrandegree = hora.get_planet_degree(float(sukranlat))   
                sukranstar = hora.star_query_english(float(sukranlat))                  
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        sukranvakram="TRUE";
                        sukrantxt="Ve(R)";
                    else:
                        sukranvakram="FALSE";
                        sukrantxt="Ve";
            elif pl == 'MARS':
                sevvailat = planets[1].strip()
                sevvaihouse = hora.get_planet_house(float(sevvailat))  
                sevvai_amsamhouse = hora.amsamrasi(float(sevvailat))
                sevvaihouse_english = hora.get_planet_house_english(float(sevvailat))
                sevvaidegree = hora.get_planet_degree(float(sevvailat))
                sevvaistar = hora.star_query_english(float(sevvailat))                 
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        sevvaivakram="TRUE";
                        sevvaitxt="Ma(R)";
                    else:
                        sevvaivakram="FALSE";
                        sevvaitxt="Ma";
            elif pl == 'JUPITER':
                gurulat = planets[1].strip()       
                guruhouse = hora.get_planet_house(float(gurulat)) 
                guru_amsamhouse = hora.amsamrasi(float(gurulat))                    
                guruhouse_english = hora.get_planet_house_english(float(gurulat))
                gurudegree = hora.get_planet_degree(float(gurulat))   
                gurustar = hora.star_query_english(float(gurulat))                         
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        guruvakram="TRUE";
                        gurutxt="Ju(R)";
                    else:
                        guruvakram="FALSE";
                        gurutxt="Ju";
            elif pl == 'SATURN':
                sanilat = planets[1].strip()    
                sanihouse = hora.get_planet_house(float(sanilat))
                sani_amsamhouse = hora.amsamrasi(float(sanilat))    
                sanihouse_english = hora.get_planet_house_english(float(sanilat))
                sanidegree = hora.get_planet_degree(float(sanilat)) 
                sanistar = hora.star_query_english(float(sanilat))                     
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        sanivakram="TRUE";
                        sanitxt="Sa(R)";
                    else:
                        sanivakram="FALSE";
                        sanitxt="Sa";
            elif pl == 'TRUE NODE':
                raghutxt="RAGHU";
                raghulat = planets[1].strip()
                raghuhouse = hora.get_planet_house(float(raghulat))  
                raghu_amsamhouse = hora.amsamrasi(float(raghulat))                        
                raghuhouse_english = hora.get_planet_house_english(float(raghulat))
                raghudegree = hora.get_planet_degree(float(raghulat))
                raghulatflt = float(planets[1].strip())  
                raghustar = hora.star_query_english(float(raghulat))                     
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    
                kethulatflt = raghulatflt + 180;
                if kethulatflt > 360:
                    kethulatflt = kethulatflt - 360;

                kethutxt="KETHU"    
                kethulat=str(round(kethulatflt,7))
                kethuhouse = hora.get_planet_house(float(kethulat)) 
                kethu_amsamhouse = hora.amsamrasi(float(kethulat))                
                kethuhouse_english = hora.get_planet_house_english(float(kethulat))
                kethudegree = hora.get_planet_degree(float(kethulat)) 
                kethustar = hora.star_query_english(float(kethulat))                     
            elif pl == 'ASCENDANT':
                lagnamtxt="LAGNAM";
                lagnamlat = planets[1].strip() 
                lagnamhouse = hora.get_planet_house(float(lagnamlat))
                lagnam_amsamhouse = hora.amsamrasi(float(lagnamlat))                
                lagnamhouse_english = hora.get_planet_house_english(float(lagnamlat))
                lagnamdegree = hora.get_planet_degree(float(lagnamlat))
                lagnamstar = hora.star_query_english(float(lagnamlat)) 
                if cnt == 4:
                    houseno = float(planets[3].strip())        
            else:
                others="Nothing"

        #print(lagnamtxt + " - " + lagnamlat)
        #print(sooriyantxt + " - " + sunlat)
        #print(chandrantxt + " - " + moonlat)
        #print(bhudhantxt + " - " + bhudhanlat)
        #print(sukrantxt + " - " + sukranlat)
        #print(sevvaitxt + " - " + sevvailat)
        #print(gurutxt + " - " + gurulat)
        #print(sanitxt + " - " + sanilat)
        #print(raghutxt + " - " + raghulat)
        #print(kethutxt + " - " + kethulat)    
                

        if lagnamhouse == "MESHAM": rasimesham.append("As")
        elif lagnamhouse == "RISHABAM": rasirishabam.append("As")
        elif lagnamhouse == "MITHUNAM": rasimithunam.append("As")
        elif lagnamhouse == "KADAGAM": rasikadagam.append("As")
        elif lagnamhouse == "SIMMAM": rasisimmam.append("As")
        elif lagnamhouse == "KANNI": rasikanni.append("As")
        elif lagnamhouse == "THULAM": rasithulam.append("As")
        elif lagnamhouse == "VIRUCHIGAM": rasiviruchigam.append("As")
        elif lagnamhouse == "DHANUSU": rasidhanusu.append("As")
        elif lagnamhouse == "MAGARAM": rasimagaram.append("As")
        elif lagnamhouse == "KUMBAM": rasikumbam.append("As")
        elif lagnamhouse == "MEENAM": rasimeenam.append("As")    


        if sunhouse == "MESHAM": rasimesham.append("Su")
        elif sunhouse == "RISHABAM": rasirishabam.append("Su")
        elif sunhouse == "MITHUNAM": rasimithunam.append("Su")
        elif sunhouse == "KADAGAM": rasikadagam.append("Su")
        elif sunhouse == "SIMMAM": rasisimmam.append("Su")
        elif sunhouse == "KANNI": rasikanni.append("Su")
        elif sunhouse == "THULAM": rasithulam.append("Su")
        elif sunhouse == "VIRUCHIGAM": rasiviruchigam.append("Su")
        elif sunhouse == "DHANUSU": rasidhanusu.append("Su")
        elif sunhouse == "MAGARAM": rasimagaram.append("Su")
        elif sunhouse == "KUMBAM": rasikumbam.append("Su")
        elif sunhouse == "MEENAM": rasimeenam.append("Su")        

        if moonhouse == "MESHAM": rasimesham.append("Mo")
        elif moonhouse == "RISHABAM": rasirishabam.append("Mo")
        elif moonhouse == "MITHUNAM": rasimithunam.append("Mo")
        elif moonhouse == "KADAGAM": rasikadagam.append("Mo")
        elif moonhouse == "SIMMAM": rasisimmam.append("Mo")
        elif moonhouse == "KANNI": rasikanni.append("Mo")
        elif moonhouse == "THULAM": rasithulam.append("Mo")
        elif moonhouse == "VIRUCHIGAM": rasiviruchigam.append("Mo")
        elif moonhouse == "DHANUSU": rasidhanusu.append("Mo")
        elif moonhouse == "MAGARAM": rasimagaram.append("Mo")
        elif moonhouse == "KUMBAM": rasikumbam.append("Mo")
        elif moonhouse == "MEENAM": rasimeenam.append("Mo")  

        if bhudhanhouse == "MESHAM": rasimesham.append(bhudhantxt)
        elif bhudhanhouse == "RISHABAM": rasirishabam.append(bhudhantxt)
        elif bhudhanhouse == "MITHUNAM": rasimithunam.append(bhudhantxt)
        elif bhudhanhouse == "KADAGAM": rasikadagam.append(bhudhantxt)
        elif bhudhanhouse == "SIMMAM": rasisimmam.append(bhudhantxt)
        elif bhudhanhouse == "KANNI": rasikanni.append(bhudhantxt)
        elif bhudhanhouse == "THULAM": rasithulam.append(bhudhantxt)
        elif bhudhanhouse == "VIRUCHIGAM": rasiviruchigam.append(bhudhantxt)
        elif bhudhanhouse == "DHANUSU": rasidhanusu.append(bhudhantxt)
        elif bhudhanhouse == "MAGARAM": rasimagaram.append(bhudhantxt)
        elif bhudhanhouse == "KUMBAM": rasikumbam.append(bhudhantxt)
        elif bhudhanhouse == "MEENAM": rasimeenam.append(bhudhantxt)  

        if sukranhouse == "MESHAM": rasimesham.append(sukrantxt)
        elif sukranhouse == "RISHABAM": rasirishabam.append(sukrantxt)
        elif sukranhouse == "MITHUNAM": rasimithunam.append(sukrantxt)
        elif sukranhouse == "KADAGAM": rasikadagam.append(sukrantxt)
        elif sukranhouse == "SIMMAM": rasisimmam.append(sukrantxt)
        elif sukranhouse == "KANNI": rasikanni.append(sukrantxt)
        elif sukranhouse == "THULAM": rasithulam.append(sukrantxt)
        elif sukranhouse == "VIRUCHIGAM": rasiviruchigam.append(sukrantxt)
        elif sukranhouse == "DHANUSU": rasidhanusu.append(sukrantxt)
        elif sukranhouse == "MAGARAM": rasimagaram.append(sukrantxt)
        elif sukranhouse == "KUMBAM": rasikumbam.append(sukrantxt)
        elif sukranhouse == "MEENAM": rasimeenam.append(sukrantxt)  
            
        if sevvaihouse == "MESHAM": rasimesham.append(sevvaitxt)
        elif sevvaihouse == "RISHABAM": rasirishabam.append(sevvaitxt)
        elif sevvaihouse == "MITHUNAM": rasimithunam.append(sevvaitxt)
        elif sevvaihouse == "KADAGAM": rasikadagam.append(sevvaitxt)
        elif sevvaihouse == "SIMMAM": rasisimmam.append(sevvaitxt)
        elif sevvaihouse == "KANNI": rasikanni.append(sevvaitxt)
        elif sevvaihouse == "THULAM": rasithulam.append(sevvaitxt)
        elif sevvaihouse == "VIRUCHIGAM": rasiviruchigam.append(sevvaitxt)
        elif sevvaihouse == "DHANUSU": rasidhanusu.append(sevvaitxt)
        elif sevvaihouse == "MAGARAM": rasimagaram.append(sevvaitxt)
        elif sevvaihouse == "KUMBAM": rasikumbam.append(sevvaitxt)
        elif sevvaihouse == "MEENAM": rasimeenam.append(sevvaitxt)              

        if guruhouse == "MESHAM": rasimesham.append(gurutxt)
        elif guruhouse == "RISHABAM": rasirishabam.append(gurutxt)
        elif guruhouse == "MITHUNAM": rasimithunam.append(gurutxt)
        elif guruhouse == "KADAGAM": rasikadagam.append(gurutxt)
        elif guruhouse == "SIMMAM": rasisimmam.append(gurutxt)
        elif guruhouse == "KANNI": rasikanni.append(gurutxt)
        elif guruhouse == "THULAM": rasithulam.append(gurutxt)
        elif guruhouse == "VIRUCHIGAM": rasiviruchigam.append(gurutxt)
        elif guruhouse == "DHANUSU": rasidhanusu.append(gurutxt)
        elif guruhouse == "MAGARAM": rasimagaram.append(gurutxt)
        elif guruhouse == "KUMBAM": rasikumbam.append(gurutxt)
        elif guruhouse == "MEENAM": rasimeenam.append(gurutxt)              

        if sanihouse == "MESHAM": rasimesham.append(sanitxt)
        elif sanihouse == "RISHABAM": rasirishabam.append(sanitxt)
        elif sanihouse == "MITHUNAM": rasimithunam.append(sanitxt)
        elif sanihouse == "KADAGAM": rasikadagam.append(sanitxt)
        elif sanihouse == "SIMMAM": rasisimmam.append(sanitxt)
        elif sanihouse == "KANNI": rasikanni.append(sanitxt)
        elif sanihouse == "THULAM": rasithulam.append(sanitxt)
        elif sanihouse == "VIRUCHIGAM": rasiviruchigam.append(sanitxt)
        elif sanihouse == "DHANUSU": rasidhanusu.append(sanitxt)
        elif sanihouse == "MAGARAM": rasimagaram.append(sanitxt)
        elif sanihouse == "KUMBAM": rasikumbam.append(sanitxt)
        elif sanihouse == "MEENAM": rasimeenam.append(sanitxt)      

        if raghuhouse == "MESHAM": rasimesham.append("Ra")
        elif raghuhouse == "RISHABAM": rasirishabam.append("Ra")
        elif raghuhouse == "MITHUNAM": rasimithunam.append("Ra")
        elif raghuhouse == "KADAGAM": rasikadagam.append("Ra")
        elif raghuhouse == "SIMMAM": rasisimmam.append("Ra")
        elif raghuhouse == "KANNI": rasikanni.append("Ra")
        elif raghuhouse == "THULAM": rasithulam.append("Ra")
        elif raghuhouse == "VIRUCHIGAM": rasiviruchigam.append("Ra")
        elif raghuhouse == "DHANUSU": rasidhanusu.append("Ra")
        elif raghuhouse == "MAGARAM": rasimagaram.append("Ra")
        elif raghuhouse == "KUMBAM": rasikumbam.append("Ra")
        elif raghuhouse == "MEENAM": rasimeenam.append("Ra")      

        if kethuhouse == "MESHAM": rasimesham.append("Ke")
        elif kethuhouse == "RISHABAM": rasirishabam.append("Ke")
        elif kethuhouse == "MITHUNAM": rasimithunam.append("Ke")
        elif kethuhouse == "KADAGAM": rasikadagam.append("Ke")
        elif kethuhouse == "SIMMAM": rasisimmam.append("Ke")
        elif kethuhouse == "KANNI": rasikanni.append("Ke")
        elif kethuhouse == "THULAM": rasithulam.append("Ke")
        elif kethuhouse == "VIRUCHIGAM": rasiviruchigam.append("Ke")
        elif kethuhouse == "DHANUSU": rasidhanusu.append("Ke")
        elif kethuhouse == "MAGARAM": rasimagaram.append("Ke")
        elif kethuhouse == "KUMBAM": rasikumbam.append("Ke")
        elif kethuhouse == "MEENAM": rasimeenam.append("Ke")      
        

        if lagnam_amsamhouse == "MESHAM": amsam_rasimesham.append("As")
        elif lagnam_amsamhouse == "RISHABAM": amsam_rasirishabam.append("As")
        elif lagnam_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("As")
        elif lagnam_amsamhouse == "KADAGAM": amsam_rasikadagam.append("As")
        elif lagnam_amsamhouse == "SIMMAM": amsam_rasisimmam.append("As")
        elif lagnam_amsamhouse == "KANNI": amsam_rasikanni.append("As")
        elif lagnam_amsamhouse == "THULAM": amsam_rasithulam.append("As")
        elif lagnam_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("As")
        elif lagnam_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("As")
        elif lagnam_amsamhouse == "MAGARAM": amsam_rasimagaram.append("As")
        elif lagnam_amsamhouse == "KUMBAM": amsam_rasikumbam.append("As")
        elif lagnam_amsamhouse == "MEENAM": amsam_rasimeenam.append("As")    


        if sun_amsamhouse == "MESHAM": amsam_rasimesham.append("Su")
        elif sun_amsamhouse == "RISHABAM": amsam_rasirishabam.append("Su")
        elif sun_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("Su")
        elif sun_amsamhouse == "KADAGAM": amsam_rasikadagam.append("Su")
        elif sun_amsamhouse == "SIMMAM": amsam_rasisimmam.append("Su")
        elif sun_amsamhouse == "KANNI": amsam_rasikanni.append("Su")
        elif sun_amsamhouse == "THULAM": amsam_rasithulam.append("Su")
        elif sun_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("Su")
        elif sun_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("Su")
        elif sun_amsamhouse == "MAGARAM": amsam_rasimagaram.append("Su")
        elif sun_amsamhouse == "KUMBAM": amsam_rasikumbam.append("Su")
        elif sun_amsamhouse == "MEENAM": amsam_rasimeenam.append("Su")        

        if moon_amsamhouse == "MESHAM": amsam_rasimesham.append("Mo")
        elif moon_amsamhouse == "RISHABAM": amsam_rasirishabam.append("Mo")
        elif moon_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("Mo")
        elif moon_amsamhouse == "KADAGAM": amsam_rasikadagam.append("Mo")
        elif moon_amsamhouse == "SIMMAM": amsam_rasisimmam.append("Mo")
        elif moon_amsamhouse == "KANNI": amsam_rasikanni.append("Mo")
        elif moon_amsamhouse == "THULAM": amsam_rasithulam.append("Mo")
        elif moon_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("Mo")
        elif moon_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("Mo")
        elif moon_amsamhouse == "MAGARAM": amsam_rasimagaram.append("Mo")
        elif moon_amsamhouse == "KUMBAM": amsam_rasikumbam.append("Mo")
        elif moon_amsamhouse == "MEENAM": amsam_rasimeenam.append("Mo")  

        if bhudhan_amsamhouse == "MESHAM": amsam_rasimesham.append(bhudhantxt)
        elif bhudhan_amsamhouse == "RISHABAM": amsam_rasirishabam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "KADAGAM": amsam_rasikadagam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "SIMMAM": amsam_rasisimmam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "KANNI": amsam_rasikanni.append(bhudhantxt)
        elif bhudhan_amsamhouse == "THULAM": amsam_rasithulam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(bhudhantxt)
        elif bhudhan_amsamhouse == "MAGARAM": amsam_rasimagaram.append(bhudhantxt)
        elif bhudhan_amsamhouse == "KUMBAM": amsam_rasikumbam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "MEENAM": amsam_rasimeenam.append(bhudhantxt)  

        if sukran_amsamhouse == "MESHAM": amsam_rasimesham.append(sukrantxt)
        elif sukran_amsamhouse == "RISHABAM": amsam_rasirishabam.append(sukrantxt)
        elif sukran_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(sukrantxt)
        elif sukran_amsamhouse == "KADAGAM": amsam_rasikadagam.append(sukrantxt)
        elif sukran_amsamhouse == "SIMMAM": amsam_rasisimmam.append(sukrantxt)
        elif sukran_amsamhouse == "KANNI": amsam_rasikanni.append(sukrantxt)
        elif sukran_amsamhouse == "THULAM": amsam_rasithulam.append(sukrantxt)
        elif sukran_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(sukrantxt)
        elif sukran_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(sukrantxt)
        elif sukran_amsamhouse == "MAGARAM": amsam_rasimagaram.append(sukrantxt)
        elif sukran_amsamhouse == "KUMBAM": amsam_rasikumbam.append(sukrantxt)
        elif sukran_amsamhouse == "MEENAM": amsam_rasimeenam.append(sukrantxt)  
            
        if sevvai_amsamhouse == "MESHAM": amsam_rasimesham.append(sevvaitxt)
        elif sevvai_amsamhouse == "RISHABAM": amsam_rasirishabam.append(sevvaitxt)
        elif sevvai_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(sevvaitxt)
        elif sevvai_amsamhouse == "KADAGAM": amsam_rasikadagam.append(sevvaitxt)
        elif sevvai_amsamhouse == "SIMMAM": amsam_rasisimmam.append(sevvaitxt)
        elif sevvai_amsamhouse == "KANNI": amsam_rasikanni.append(sevvaitxt)
        elif sevvai_amsamhouse == "THULAM": amsam_rasithulam.append(sevvaitxt)
        elif sevvai_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(sevvaitxt)
        elif sevvai_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(sevvaitxt)
        elif sevvai_amsamhouse == "MAGARAM": amsam_rasimagaram.append(sevvaitxt)
        elif sevvai_amsamhouse == "KUMBAM": amsam_rasikumbam.append(sevvaitxt)
        elif sevvai_amsamhouse == "MEENAM": amsam_rasimeenam.append(sevvaitxt)              

        if guru_amsamhouse == "MESHAM": amsam_rasimesham.append(gurutxt)
        elif guru_amsamhouse == "RISHABAM": amsam_rasirishabam.append(gurutxt)
        elif guru_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(gurutxt)
        elif guru_amsamhouse == "KADAGAM": amsam_rasikadagam.append(gurutxt)
        elif guru_amsamhouse == "SIMMAM": amsam_rasisimmam.append(gurutxt)
        elif guru_amsamhouse == "KANNI": amsam_rasikanni.append(gurutxt)
        elif guru_amsamhouse == "THULAM": amsam_rasithulam.append(gurutxt)
        elif guru_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(gurutxt)
        elif guru_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(gurutxt)
        elif guru_amsamhouse == "MAGARAM": amsam_rasimagaram.append(gurutxt)
        elif guru_amsamhouse == "KUMBAM": amsam_rasikumbam.append(gurutxt)
        elif guru_amsamhouse == "MEENAM": amsam_rasimeenam.append(gurutxt)              

        if sani_amsamhouse == "MESHAM": amsam_rasimesham.append(sanitxt)
        elif sani_amsamhouse == "RISHABAM": amsam_rasirishabam.append(sanitxt)
        elif sani_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(sanitxt)
        elif sani_amsamhouse == "KADAGAM": amsam_rasikadagam.append(sanitxt)
        elif sani_amsamhouse == "SIMMAM": amsam_rasisimmam.append(sanitxt)
        elif sani_amsamhouse == "KANNI": amsam_rasikanni.append(sanitxt)
        elif sani_amsamhouse == "THULAM": amsam_rasithulam.append(sanitxt)
        elif sani_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(sanitxt)
        elif sani_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(sanitxt)
        elif sani_amsamhouse == "MAGARAM": amsam_rasimagaram.append(sanitxt)
        elif sani_amsamhouse == "KUMBAM": amsam_rasikumbam.append(sanitxt)
        elif sani_amsamhouse == "MEENAM": amsam_rasimeenam.append(sanitxt)      

        if raghu_amsamhouse == "MESHAM": amsam_rasimesham.append("Ra")
        elif raghu_amsamhouse == "RISHABAM": amsam_rasirishabam.append("Ra")
        elif raghu_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("Ra")
        elif raghu_amsamhouse == "KADAGAM": amsam_rasikadagam.append("Ra")
        elif raghu_amsamhouse == "SIMMAM": amsam_rasisimmam.append("Ra")
        elif raghu_amsamhouse == "KANNI": amsam_rasikanni.append("Ra")
        elif raghu_amsamhouse == "THULAM": amsam_rasithulam.append("Ra")
        elif raghu_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("Ra")
        elif raghu_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("Ra")
        elif raghu_amsamhouse == "MAGARAM": amsam_rasimagaram.append("Ra")
        elif raghu_amsamhouse == "KUMBAM": amsam_rasikumbam.append("Ra")
        elif raghu_amsamhouse == "MEENAM": amsam_rasimeenam.append("Ra")      

        if kethu_amsamhouse == "MESHAM": amsam_rasimesham.append("Ke")
        elif kethu_amsamhouse == "RISHABAM": amsam_rasirishabam.append("Ke")
        elif kethu_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("Ke")
        elif kethu_amsamhouse == "KADAGAM": amsam_rasikadagam.append("Ke")
        elif kethu_amsamhouse == "SIMMAM": amsam_rasisimmam.append("Ke")
        elif kethu_amsamhouse == "KANNI": amsam_rasikanni.append("Ke")
        elif kethu_amsamhouse == "THULAM": amsam_rasithulam.append("Ke")
        elif kethu_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("Ke")
        elif kethu_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("Ke")
        elif kethu_amsamhouse == "MAGARAM": amsam_rasimagaram.append("Ke")
        elif kethu_amsamhouse == "KUMBAM": amsam_rasikumbam.append("Ke")
        elif kethu_amsamhouse == "MEENAM": amsam_rasimeenam.append("Ke")              
        #print(rasimesham)
        #print(rasirishabam)
        #print(rasimithunam)
        #print(rasikadagam)
        #print(rasisimmam)
        #print(rasikanni)
        #print(rasithulam)
        #print(rasiviruchigam)
        #print(rasidhanusu)
        #print(rasimagaram)    
        #print(rasikumbam)
        #print(rasimeenam)
        #print("  ")

        rasivalues_global = []
        rasivalues_global.append((hora.p1_format(rasimesham)))
        rasivalues_global.append((hora.p1_format(rasirishabam)))
        rasivalues_global.append((hora.p1_format(rasimithunam)))
        rasivalues_global.append((hora.p1_format(rasikadagam)))
        rasivalues_global.append((hora.p1_format(rasisimmam)))
        rasivalues_global.append((hora.p1_format(rasikanni)))
        rasivalues_global.append((hora.p1_format(rasithulam)))
        rasivalues_global.append((hora.p1_format(rasiviruchigam)))
        rasivalues_global.append((hora.p1_format(rasidhanusu)))
        rasivalues_global.append((hora.p1_format(rasimagaram)))
        rasivalues_global.append((hora.p1_format(rasikumbam)))
        rasivalues_global.append((hora.p1_format(rasimeenam)))
        
        
        amsamvalues_global = []
        amsamvalues_global.append(hora.p1_format(amsam_rasimesham))
        amsamvalues_global.append(hora.p1_format(amsam_rasirishabam))
        amsamvalues_global.append(hora.p1_format(amsam_rasimithunam))
        amsamvalues_global.append(hora.p1_format(amsam_rasikadagam))
        amsamvalues_global.append(hora.p1_format(amsam_rasisimmam))
        amsamvalues_global.append(hora.p1_format(amsam_rasikanni))
        amsamvalues_global.append(hora.p1_format(amsam_rasithulam))
        amsamvalues_global.append(hora.p1_format(amsam_rasiviruchigam))
        amsamvalues_global.append(hora.p1_format(amsam_rasidhanusu))
        amsamvalues_global.append(hora.p1_format(amsam_rasimagaram))
        amsamvalues_global.append(hora.p1_format(amsam_rasikumbam))
        amsamvalues_global.append(hora.p1_format(amsam_rasimeenam))

            

        
        fnt = QFont('Arial', 12)
        fnta = QFont('Arial', 12)
        
        self.rasi_mesham_lbl.setFont(fnt)
        self.rasi_rishabam_lbl.setFont(fnt)
        self.rasi_mithunam_lbl.setFont(fnt)
        self.rasi_kadagam_lbl.setFont(fnt)
        self.rasi_simmam_lbl.setFont(fnt)
        self.rasi_kanni_lbl.setFont(fnt)
        self.rasi_thulam_lbl.setFont(fnt)
        self.rasi_viruchigam_lbl.setFont(fnt)
        self.rasi_dhanusu_lbl.setFont(fnt)
        self.rasi_magaram_lbl.setFont(fnt)
        self.rasi_kumbam_lbl.setFont(fnt)
        self.rasi_meenam_lbl.setFont(fnt)
        self.rasi_center_lbl.setFont(fnta)        

        
        self.rasi_mesham_lbl.setText(hora.p_format(rasimesham))
        self.rasi_rishabam_lbl.setText(hora.p_format(rasirishabam))
        self.rasi_mithunam_lbl.setText(hora.p_format(rasimithunam))
        self.rasi_kadagam_lbl.setText(hora.p_format(rasikadagam))
        self.rasi_simmam_lbl.setText(hora.p_format(rasisimmam))
        self.rasi_kanni_lbl.setText(hora.p_format(rasikanni))
        self.rasi_thulam_lbl.setText(hora.p_format(rasithulam))
        self.rasi_viruchigam_lbl.setText(hora.p_format(rasiviruchigam))
        self.rasi_dhanusu_lbl.setText(hora.p_format(rasidhanusu))
        self.rasi_magaram_lbl.setText(hora.p_format(rasimagaram))
        self.rasi_kumbam_lbl.setText(hora.p_format(rasikumbam))
        self.rasi_meenam_lbl.setText(hora.p_format(rasimeenam))
        self.rasi_center_lbl.setText("RASI")
        

        self.amsam_mesham_lbl.setFont(fnt)
        self.amsam_rishabam_lbl.setFont(fnt)
        self.amsam_mithunam_lbl.setFont(fnt)
        self.amsam_kadagam_lbl.setFont(fnt)
        self.amsam_simmam_lbl.setFont(fnt)
        self.amsam_kanni_lbl.setFont(fnt)
        self.amsam_thulam_lbl.setFont(fnt)
        self.amsam_viruchigam_lbl.setFont(fnt)
        self.amsam_dhanusu_lbl.setFont(fnt)
        self.amsam_magaram_lbl.setFont(fnt)
        self.amsam_kumbam_lbl.setFont(fnt)
        self.amsam_meenam_lbl.setFont(fnt)
        self.amsam_center_lbl.setFont(fnta)
        
        self.amsam_mesham_lbl.setText(hora.p_format(amsam_rasimesham))
        self.amsam_rishabam_lbl.setText(hora.p_format(amsam_rasirishabam))
        self.amsam_mithunam_lbl.setText(hora.p_format(amsam_rasimithunam))
        self.amsam_kadagam_lbl.setText(hora.p_format(amsam_rasikadagam))
        self.amsam_simmam_lbl.setText(hora.p_format(amsam_rasisimmam))
        self.amsam_kanni_lbl.setText(hora.p_format(amsam_rasikanni))
        self.amsam_thulam_lbl.setText(hora.p_format(amsam_rasithulam))
        self.amsam_viruchigam_lbl.setText(hora.p_format(amsam_rasiviruchigam))
        self.amsam_dhanusu_lbl.setText(hora.p_format(amsam_rasidhanusu))
        self.amsam_magaram_lbl.setText(hora.p_format(amsam_rasimagaram))
        self.amsam_kumbam_lbl.setText(hora.p_format(amsam_rasikumbam))
        self.amsam_meenam_lbl.setText(hora.p_format(amsam_rasimeenam))
        self.amsam_center_lbl.setText("NAVAMSAM")
            
        fnt = QFont('Arial', 12)

        self.tableWidget.setRowCount(0);
        self.tableWidget.setColumnCount(0);
        self.tableWidget.setRowCount(10);
        self.tableWidget.setColumnCount(5);
        
        self.tableWidget.setFont(fnt);
        
        self.tableWidget.setHorizontalHeaderLabels(['Zodiac','Degree','Star','Star Lord','Longitude'])
        self.tableWidget.setVerticalHeaderLabels(['Ascendent','Sun','Moon','Mercury','Venus','Mars','Jupiter','Saturn','Raghu','Kethu'])

        #header = self.tableWidget.horizontalHeader()       
        #header.setSectionResizeMode(0, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(1, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(2, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(3, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(4, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(5, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(6, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(7, qtw.QHeaderView.Stretch)
        self.tableWidget.setColumnWidth(0, 70)        
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 70)        
        self.tableWidget.setColumnWidth(3, 70)
        self.tableWidget.setColumnWidth(4, 70)
        
        self.tableWidget.setItem(0,0, QTableWidgetItem(lagnamhouse_english)) 
        self.tableWidget.setItem(1,0, QTableWidgetItem(sunhouse_english))         
        self.tableWidget.setItem(2,0, QTableWidgetItem(moonhouse_english))         
        self.tableWidget.setItem(3,0, QTableWidgetItem(bhudhanhouse_english))         
        self.tableWidget.setItem(4,0, QTableWidgetItem(sukranhouse_english))         
        self.tableWidget.setItem(5,0, QTableWidgetItem(sevvaihouse_english))         
        self.tableWidget.setItem(6,0, QTableWidgetItem(guruhouse_english))  
        self.tableWidget.setItem(7,0, QTableWidgetItem(sanihouse_english))         
        self.tableWidget.setItem(8,0, QTableWidgetItem(raghuhouse_english))         
        self.tableWidget.setItem(9,0, QTableWidgetItem(kethuhouse_english))        


        self.tableWidget.setItem(0,1, QTableWidgetItem(lagnamdegree)) 
        self.tableWidget.setItem(1,1, QTableWidgetItem(sundegree))         
        self.tableWidget.setItem(2,1, QTableWidgetItem(moondegree))         
        self.tableWidget.setItem(3,1, QTableWidgetItem(bhudhandegree))         
        self.tableWidget.setItem(4,1, QTableWidgetItem(sukrandegree))         
        self.tableWidget.setItem(5,1, QTableWidgetItem(sevvaidegree))         
        self.tableWidget.setItem(6,1, QTableWidgetItem(gurudegree))  
        self.tableWidget.setItem(7,1, QTableWidgetItem(sanidegree))         
        self.tableWidget.setItem(8,1, QTableWidgetItem(raghudegree))         
        self.tableWidget.setItem(9,1, QTableWidgetItem(kethudegree))      

        lagnamstarpadam = lagnamstar + " - " + str(hora.star_padam(float(lagnamlat)))
        sunstarpadam = sunstar + " - " + str(hora.star_padam(float(sunlat)))
        moonstarpadam = moonstar + " - " + str(hora.star_padam(float(moonlat)))
        bhudhanstarpadam = bhudhanstar + " - " + str(hora.star_padam(float(bhudhanlat)))
        sukranstarpadam = sukranstar + " - " + str(hora.star_padam(float(sukranlat)))
        sevvaistarpadam = sevvaistar + " - " + str(hora.star_padam(float(sevvailat)))
        gurustarpadam = gurustar + " - " + str(hora.star_padam(float(gurulat)))
        sanistarpadam = sanistar + " - " + str(hora.star_padam(float(sanilat)))
        raghustarpadam = raghustar + " - " + str(hora.star_padam(float(raghulat)))
        kethustarpadam = kethustar + " - " + str(hora.star_padam(float(kethulat)))

        
        self.tableWidget.setItem(0,2, QTableWidgetItem(lagnamstarpadam)) 
        self.tableWidget.setItem(1,2, QTableWidgetItem(sunstarpadam))         
        self.tableWidget.setItem(2,2, QTableWidgetItem(moonstarpadam))         
        self.tableWidget.setItem(3,2, QTableWidgetItem(bhudhanstarpadam))         
        self.tableWidget.setItem(4,2, QTableWidgetItem(sukranstarpadam))         
        self.tableWidget.setItem(5,2, QTableWidgetItem(sevvaistarpadam))         
        self.tableWidget.setItem(6,2, QTableWidgetItem(gurustarpadam))  
        self.tableWidget.setItem(7,2, QTableWidgetItem(sanistarpadam))         
        self.tableWidget.setItem(8,2, QTableWidgetItem(raghustarpadam))         
        self.tableWidget.setItem(9,2, QTableWidgetItem(kethustarpadam))      


        
        self.tableWidget.setItem(0,3, QTableWidgetItem(hora.star_lord(float(lagnamlat))))
        self.tableWidget.setItem(1,3, QTableWidgetItem(hora.star_lord(float(sunlat))))         
        self.tableWidget.setItem(2,3, QTableWidgetItem(hora.star_lord(float(moonlat))))         
        self.tableWidget.setItem(3,3, QTableWidgetItem(hora.star_lord(float(bhudhanlat))))        
        self.tableWidget.setItem(4,3, QTableWidgetItem(hora.star_lord(float(sukranlat))))         
        self.tableWidget.setItem(5,3, QTableWidgetItem(hora.star_lord(float(sevvailat))))         
        self.tableWidget.setItem(6,3, QTableWidgetItem(hora.star_lord(float(gurulat))))  
        self.tableWidget.setItem(7,3, QTableWidgetItem(hora.star_lord(float(sanilat))))         
        self.tableWidget.setItem(8,3, QTableWidgetItem(hora.star_lord(float(raghulat))))         
        self.tableWidget.setItem(9,3, QTableWidgetItem(hora.star_lord(float(kethulat))))


        self.tableWidget.setItem(0,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(lagnamlat))))
        self.tableWidget.setItem(1,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(sunlat))))         
        self.tableWidget.setItem(2,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(moonlat))))         
        self.tableWidget.setItem(3,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(bhudhanlat))))        
        self.tableWidget.setItem(4,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(sukranlat))))         
        self.tableWidget.setItem(5,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(sevvailat))))         
        self.tableWidget.setItem(6,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(gurulat))))  
        self.tableWidget.setItem(7,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(sanilat))))         
        self.tableWidget.setItem(8,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(raghulat))))         
        self.tableWidget.setItem(9,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(kethulat))))

        
        native_name = self.lineEdit_Nativename.text()
        native_sex = self.comboBox_Sex.currentText()
        native_date = self.dateEdit_Dob.date()
        native_time = self.timeEdit_Btime.time()
        native_day = native_date.day()
        native_month = native_date.month()
        native_year = native_date.year()
        native_hour = native_time.toString("hh")
        native_minutes = native_time.toString("mm")
        native_seconds = native_time.toString("ss")
        native_birthplace = self.lineEdit_Birthplace.text()
        native_timezone = self.comboBox_Timezone.currentText()
        native_longdeg = self.lineEdit_Longitudedeg.text()
        native_longdir = self.comboBox_Longitudedir.currentText()
        native_longmin = self.lineEdit_Longitudemin.text()
        native_latdeg = self.lineEdit_Lattitudedeg.text()
        native_latdir = self.comboBox_Lattitudedir.currentText()
        native_latmin = self.lineEdit_Lattitudemin.text()
        native_language = self.comboBox_Language.currentText()
        tp_date = str(native_day) + "/" + str(native_month) + "/" + str(native_year)   
        py_date = str(native_year) + ", " + str(native_month) + ", " +     str(native_day) 
        tp_time_print =    native_hour + ":" + native_minutes + ":" + native_seconds 
        
        if native_name=="":
            native_name="Current Transit"

        native_text = "<h4>Native Details</h4><table><tr><td>Name: </td><td>" + native_name + "</td></tr><tr><td>Sex: </td><td>" + self.comboBox_Sex.currentText() + "</td></tr><tr><td>Date: </td><td>" + tp_date + "</td></tr><tr><td>Time: </td><td>" + native_hour + ":" + native_minutes + ":" + native_seconds + "</td></tr><tr><td>Place: </td><td>" + self.lineEdit_Birthplace.text() + "</td></tr></table>"
        native_birth_array = native_birthplace.split("-")        
        native_birthplace_1 = native_birth_array[0]
        
        txt=""
        thithi = hora.find_thithi(moonlat, sunlat,"english")
        yoga = hora.find_yoga(moonlat, sunlat,"english")
        karnam = hora.find_karnam(moonlat, sunlat, "english")
        
        dateobj = datetime.date(native_year, native_month, native_day)

        
        dasavalues = self.dasabhukthitree(float(moonlat),tp_date,"english")
        dasavalues = "<table><tr><td width=100%>" + dasavalues + "</td></tr></table>"

        
        panjangam_text = "<h4>Panjangam</h4><table><tr><td>Lagna: </td><td>" + lagnamhouse_english + "</td></tr><tr><td>Rasi: </td><td>" + moonhouse_english + "</td></tr><tr><td>Star: </td><td>" + moonstar + "</td></tr><tr><td>Thithi: </td><td>" + thithi + "</td></tr><tr><td>Karna: </td><td>" + karnam + "</td></tr><tr><td>Yoga: </td><td>" + yoga + "</td></tr><tr><td>Day: </td><td>" + dateobj.strftime('%A') + "</td></tr></table>"
        
        panjangam_text = panjangam_text + "<br>" + dasavalues
        
        print_head = self.lineEdit_Nativename.text()
        if print_head=="":
            print_head ="Current Transit Horoscope"
        else:
            print_head = print_head + ""
                
      

        self.label_panjangam.setFont(fnt)
        self.label_dasa.setFont(fnt)
        
        self.label_panjangam.setText(native_text)
        self.label_dasa.setText(panjangam_text)
        

        nameletters = hora.namelettersenglish(hora.star_query(float(moonlat)))
        startrees = hora.startreesenglish(hora.star_query(float(moonlat)))
        
        print_essentials = []
        print_essentials.append(print_head)
        print_essentials.append(native_sex)
        print_essentials.append(tp_date)        
        print_essentials.append(tp_time_print)        
        print_essentials.append(native_birthplace_1)
        print_essentials.append(lagnamhouse_english)
        print_essentials.append(moonhouse_english)
        print_essentials.append(moonstar)         
        print_essentials.append(thithi)    
        print_essentials.append(karnam)            
        print_essentials.append(yoga)    
        print_essentials.append(dateobj.strftime('%A'))            
        print_essentials.append(dasavalues)
        print_essentials.append(nameletters)
        print_essentials.append(startrees)
        
        
        planettable_html = "<table><tr><th width='16%'>Planet</th><th width='16%'>Lattitude</th><th width='14%'>Zodiac</th><th width='14%'>Degree</th><th width='26%'>Star</th><th width='14%'>Star Lord</th></tr><tr><td>" + "Ascendent" + "</td><td>" + hora.Convert_Longitude_into_time(float(lagnamlat)) + "</td><td>" + lagnamhouse_english +"</td><td>" + lagnamdegree +"</td><td>" + lagnamstarpadam +"</td><td>" + hora.star_lord(float(lagnamlat)) +"</td></tr><tr><td>" + 'Sun' + "</td><td>"+hora.Convert_Longitude_into_time(float(sunlat))+"</td><td>"+sunhouse_english+"</td><td>"+sundegree+"</td><td>"+sunstarpadam+"</td><td>" + hora.star_lord(float(sunlat)) +"</td></tr><tr><td>"+ 'Moon' +"</td><td>"+hora.Convert_Longitude_into_time(float(moonlat))+"</td><td>"+moonhouse_english+"</td><td>"+moondegree+"</td><td>"+moonstarpadam+"</td><td>" + hora.star_lord(float(moonlat)) +"</td></tr><tr><td>" +'Mercury' + "</td><td>"+hora.Convert_Longitude_into_time(float(bhudhanlat))+"</td><td>"+bhudhanhouse_english+"</td><td>"+bhudhandegree+"</td><td>"+bhudhanstarpadam+"</td><td>" + hora.star_lord(float(bhudhanlat)) +"</td></tr><tr><td>"+ 'Venus' +"</td><td>"+hora.Convert_Longitude_into_time(float(sukranlat))+"</td><td>"+sukranhouse_english+"</td><td>"+sukrandegree+"</td><td>"+sukranstarpadam+"</td><td>" + hora.star_lord(float(sukranlat)) +"</td></tr><tr><td>" + 'Mars' +"</td><td>"+hora.Convert_Longitude_into_time(float(sevvailat))+"</td><td>"+sevvaihouse_english+"</td><td>"+sevvaidegree+"</td><td>"+sevvaistarpadam+"</td><td>" + hora.star_lord(float(sevvailat)) +"</td></tr><tr><td>"+ 'Jupiter' +"</td><td>"+hora.Convert_Longitude_into_time(float(gurulat))+"</td><td>"+guruhouse_english+"</td><td>"+gurudegree+"</td><td>"+gurustarpadam+"</td><td>" + hora.star_lord(float(gurulat)) +"</td></tr><tr><td>"+'Saturn' +"</td><td>"+hora.Convert_Longitude_into_time(float(sanilat))+"</td><td>"+sanihouse_english+"</td><td>"+sanidegree+"</td><td>"+sanistarpadam+"</td><td>" + hora.star_lord(float(sanilat)) +"</td></tr><tr><td>"+'Raghu' +"</td><td>"+hora.Convert_Longitude_into_time(float(raghulat))+"</td><td>"+raghuhouse_english+"</td><td>"+raghudegree+"</td><td>"+raghustarpadam+"</td><td>" + hora.star_lord(float(raghulat)) +"</td></tr><tr><td>"+'Kethu' +"</td><td>"+hora.Convert_Longitude_into_time(float(kethulat))+"</td><td>"+kethuhouse_english +"</td><td>"+kethudegree+"</td><td>"+kethustarpadam+"</td><td>" + hora.star_lord(float(kethulat)) +"</td></tr></table>"
        
        self.preview.build_horoscope("english",rasivalues_global,amsamvalues_global,planettable_html, print_essentials)
        
        
    def horoscope_tamil(self, p_date, p_time, p_longitude, p_latitude):
        #txtcmd = "swetest -edire: -b29.10.1977 -ut16:00 -p0123456789tm -house80.28333333,13.08333333,O -eswe -fPlLs -g, -n1 -s1 -sid1 -head"

        txtcmd = "swetest -edire: -b" + p_date + " -ut" + p_time + " -p0123456789tm -house" + p_longitude + "," + p_latitude + ",O -eswe -fPlLs -g, -n1 -s1 -sid1 -head"
        
        batcmd = txtcmd
        
        result_code = os.system(batcmd + ' > output.txt')
        if os.path.exists('output.txt'):
            fp = open('output.txt', "r")

        Lines = fp.readlines() 
  
        count = 0
        arr = []

        # Strips the newline character 
        for line in Lines: 
            arr.append(line.strip())

        lagnamtxt=""
        lagnamlat=""
        chandrantxt=""
        moonlat=""
        sooriyantxt=""
        sunlat=""
        bhudhantxt=""
        bhudhanlat=""
        bhudhanvakram=""
        sukrantxt=""
        sukranlat=""
        sukranvakram=""
        sevvaitxt=""
        sevvailat=""
        sevvaivakram=""
        gurutxt=""
        gurulat=""
        guruvakram=""
        sanitxt=""
        sanilat=""
        sanivakram=""
        raghutxt=""
        raghulat=""
        kethutxt=""
        kethulat=""

        rasimesham = []
        rasirishabam = []
        rasimithunam = []
        rasikadagam = []
        rasisimmam = []
        rasikanni = []
        rasithulam =  []
        rasiviruchigam = []
        rasidhanusu = []
        rasimagaram = []
        rasikumbam = []
        rasimeenam = []
        
        amsam_rasimesham = []
        amsam_rasirishabam = []
        amsam_rasimithunam = []
        amsam_rasikadagam = []
        amsam_rasisimmam = []
        amsam_rasikanni = []
        amsam_rasithulam =  []
        amsam_rasiviruchigam = []
        amsam_rasidhanusu = []
        amsam_rasimagaram = []
        amsam_rasikumbam = []
        amsam_rasimeenam = []        
        
    
        for x in arr:
            planets = x.split(",");    
            cnt = len(planets)

            pl = planets[0].strip().upper();
            

                
            if pl == 'MOON':
                chandrantxt = "MOON"
                moonlat = planets[1].strip()
                moonhouse = hora.get_planet_house(float(moonlat))
                moon_amsamhouse = hora.amsamrasi(float(moonlat))         
                moonhouse_tamil = hora.get_planet_house_tamil(float(moonlat))
                moondegree = hora.get_planet_degree(float(moonlat))    
                moonstar = hora.star_query_english(float(moonlat))   
                moonstar_tamil = hora.star_query_tamil(float(moonlat))                  
            elif pl == 'SUN':
                sooriyantxt="SUN"
                sunlat = planets[1].strip()
                sunhouse = hora.get_planet_house(float(sunlat))  
                sun_amsamhouse = hora.amsamrasi(float(sunlat))      
                sunhouse_tamil = hora.get_planet_house_tamil(float(sunlat))   
                sundegree = hora.get_planet_degree(float(sunlat))    
                sunstar = hora.star_query_english(float(sunlat)) 
                sunstar_tamil = hora.star_query_tamil(float(sunlat))                 
            elif pl == 'MERCURY':
                bhudhanlat = planets[1].strip()
                bhudhanhouse = hora.get_planet_house(float(bhudhanlat))
                bhudhan_amsamhouse = hora.amsamrasi(float(bhudhanlat))
                bhudhanhouse_tamil = hora.get_planet_house_tamil(float(bhudhanlat))
                bhudhandegree = hora.get_planet_degree(float(bhudhanlat))
                bhudhanstar = hora.star_query_english(float(bhudhanlat))  
                bhudhanstar_tamil = hora.star_query_tamil(float(bhudhanlat))  
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        bhudhanvakram="TRUE";
                        bhudhantxt="புத(வ)";
                    else:
                        bhudhanvakram="FALSE";
                        bhudhantxt="புத";
            elif pl == 'VENUS':
                sukranlat = planets[1].strip()
                sukranhouse = hora.get_planet_house(float(sukranlat))
                sukran_amsamhouse = hora.amsamrasi(float(sukranlat))
                sukranhouse_tamil = hora.get_planet_house_tamil(float(sukranlat))
                sukrandegree = hora.get_planet_degree(float(sukranlat))   
                sukranstar = hora.star_query_english(float(sukranlat))   
                sukranstar_tamil = hora.star_query_tamil(float(sukranlat))
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        sukranvakram="TRUE";
                        sukrantxt="சுக்(வ)";
                    else:
                        sukranvakram="FALSE";
                        sukrantxt="சுக்";
            elif pl == 'MARS':
                sevvailat = planets[1].strip()
                sevvaihouse = hora.get_planet_house(float(sevvailat))  
                sevvai_amsamhouse = hora.amsamrasi(float(sevvailat))
                sevvaihouse_tamil = hora.get_planet_house_tamil(float(sevvailat))  
                sevvaidegree = hora.get_planet_degree(float(sevvailat))
                sevvaistar = hora.star_query_english(float(sevvailat))    
                sevvaistar_tamil = hora.star_query_tamil(float(sevvailat))
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        sevvaivakram="TRUE";
                        sevvaitxt="செவ்(வ)";
                    else:
                        sevvaivakram="FALSE";
                        sevvaitxt="செவ்";
            elif pl == 'JUPITER':
                gurulat = planets[1].strip()       
                guruhouse = hora.get_planet_house(float(gurulat))
                guru_amsamhouse = hora.amsamrasi(float(gurulat))   
                guruhouse_tamil = hora.get_planet_house_tamil(float(gurulat))   
                gurudegree = hora.get_planet_degree(float(gurulat))   
                gurustar = hora.star_query_english(float(gurulat)) 
                gurustar_tamil = hora.star_query_tamil(float(gurulat))      
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        guruvakram="TRUE";
                        gurutxt="குரு(வ)";
                    else:
                        guruvakram="FALSE";
                        gurutxt="குரு";
            elif pl == 'SATURN':
                sanilat = planets[1].strip()    
                sanihouse = hora.get_planet_house(float(sanilat))
                sani_amsamhouse = hora.amsamrasi(float(sanilat))   
                sanihouse_tamil = hora.get_planet_house_tamil(float(sanilat))
                sanidegree = hora.get_planet_degree(float(sanilat)) 
                sanistar = hora.star_query_english(float(sanilat)) 
                sanistar_tamil = hora.star_query_tamil(float(sanilat))                 
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    if houseno < 0:
                        sanivakram="TRUE";
                        sanitxt="சனி(வ)";
                    else:
                        sanivakram="FALSE";
                        sanitxt="சனி";
            elif pl == 'TRUE NODE':
                raghutxt="RAGHU";
                raghulat = planets[1].strip()
                raghuhouse = hora.get_planet_house(float(raghulat)) 
                raghu_amsamhouse = hora.amsamrasi(float(raghulat))  
                raghuhouse_tamil = hora.get_planet_house_tamil(float(raghulat))
                raghudegree = hora.get_planet_degree(float(raghulat))
                raghulatflt = float(planets[1].strip())  
                raghustar = hora.star_query_english(float(raghulat)) 
                raghustar_tamil = hora.star_query_tamil(float(raghulat))                 
                if cnt == 4:
                    houseno = float(planets[3].strip())
                    
                kethulatflt = raghulatflt + 180;
                if kethulatflt > 360:
                    kethulatflt = kethulatflt - 360;

                kethutxt="KETHU"    
                kethulat=str(round(kethulatflt,7))
                kethuhouse = hora.get_planet_house(float(kethulat)) 
                kethu_amsamhouse = hora.amsamrasi(float(kethulat))      
                kethuhouse_tamil = hora.get_planet_house_tamil(float(kethulat)) 
                kethudegree = hora.get_planet_degree(float(kethulat)) 
                kethustar = hora.star_query_english(float(kethulat))    
                kethustar_tamil = hora.star_query_tamil(float(kethulat))                  
            elif pl == 'ASCENDANT':
                lagnamtxt="LAGNAM";
                lagnamlat = planets[1].strip() 
                lagnamhouse = hora.get_planet_house(float(lagnamlat)) 
                lagnam_amsamhouse = hora.amsamrasi(float(lagnamlat))    
                lagnamhouse_tamil = hora.get_planet_house_tamil(float(lagnamlat))  
                lagnamdegree = hora.get_planet_degree(float(lagnamlat))
                lagnamstar = hora.star_query_english(float(lagnamlat)) 
                lagnamstar_tamil = hora.star_query_tamil(float(lagnamlat)) 
                if cnt == 4:
                    houseno = float(planets[3].strip())        
            else:
                others="Nothing"
        

        if lagnamhouse == "MESHAM": rasimesham.append("லக்")
        elif lagnamhouse == "RISHABAM": rasirishabam.append("லக்")
        elif lagnamhouse == "MITHUNAM": rasimithunam.append("லக்")
        elif lagnamhouse == "KADAGAM": rasikadagam.append("லக்")
        elif lagnamhouse == "SIMMAM": rasisimmam.append("லக்")
        elif lagnamhouse == "KANNI": rasikanni.append("லக்")
        elif lagnamhouse == "THULAM": rasithulam.append("லக்")
        elif lagnamhouse == "VIRUCHIGAM": rasiviruchigam.append("லக்")
        elif lagnamhouse == "DHANUSU": rasidhanusu.append("லக்")
        elif lagnamhouse == "MAGARAM": rasimagaram.append("லக்")
        elif lagnamhouse == "KUMBAM": rasikumbam.append("லக்")
        elif lagnamhouse == "MEENAM": rasimeenam.append("லக்")    


        if sunhouse == "MESHAM": rasimesham.append("சூரி")
        elif sunhouse == "RISHABAM": rasirishabam.append("சூரி")
        elif sunhouse == "MITHUNAM": rasimithunam.append("சூரி")
        elif sunhouse == "KADAGAM": rasikadagam.append("சூரி")
        elif sunhouse == "SIMMAM": rasisimmam.append("சூரி")
        elif sunhouse == "KANNI": rasikanni.append("சூரி")
        elif sunhouse == "THULAM": rasithulam.append("சூரி")
        elif sunhouse == "VIRUCHIGAM": rasiviruchigam.append("சூரி")
        elif sunhouse == "DHANUSU": rasidhanusu.append("சூரி")
        elif sunhouse == "MAGARAM": rasimagaram.append("சூரி")
        elif sunhouse == "KUMBAM": rasikumbam.append("சூரி")
        elif sunhouse == "MEENAM": rasimeenam.append("சூரி")        

        if moonhouse == "MESHAM": rasimesham.append("சந்")
        elif moonhouse == "RISHABAM": rasirishabam.append("சந்")
        elif moonhouse == "MITHUNAM": rasimithunam.append("சந்")
        elif moonhouse == "KADAGAM": rasikadagam.append("சந்")
        elif moonhouse == "SIMMAM": rasisimmam.append("சந்")
        elif moonhouse == "KANNI": rasikanni.append("சந்")
        elif moonhouse == "THULAM": rasithulam.append("சந்")
        elif moonhouse == "VIRUCHIGAM": rasiviruchigam.append("சந்")
        elif moonhouse == "DHANUSU": rasidhanusu.append("சந்")
        elif moonhouse == "MAGARAM": rasimagaram.append("சந்")
        elif moonhouse == "KUMBAM": rasikumbam.append("சந்")
        elif moonhouse == "MEENAM": rasimeenam.append("சந்")  

        if bhudhanhouse == "MESHAM": rasimesham.append(bhudhantxt)
        elif bhudhanhouse == "RISHABAM": rasirishabam.append(bhudhantxt)
        elif bhudhanhouse == "MITHUNAM": rasimithunam.append(bhudhantxt)
        elif bhudhanhouse == "KADAGAM": rasikadagam.append(bhudhantxt)
        elif bhudhanhouse == "SIMMAM": rasisimmam.append(bhudhantxt)
        elif bhudhanhouse == "KANNI": rasikanni.append(bhudhantxt)
        elif bhudhanhouse == "THULAM": rasithulam.append(bhudhantxt)
        elif bhudhanhouse == "VIRUCHIGAM": rasiviruchigam.append(bhudhantxt)
        elif bhudhanhouse == "DHANUSU": rasidhanusu.append(bhudhantxt)
        elif bhudhanhouse == "MAGARAM": rasimagaram.append(bhudhantxt)
        elif bhudhanhouse == "KUMBAM": rasikumbam.append(bhudhantxt)
        elif bhudhanhouse == "MEENAM": rasimeenam.append(bhudhantxt)  

        if sukranhouse == "MESHAM": rasimesham.append(sukrantxt)
        elif sukranhouse == "RISHABAM": rasirishabam.append(sukrantxt)
        elif sukranhouse == "MITHUNAM": rasimithunam.append(sukrantxt)
        elif sukranhouse == "KADAGAM": rasikadagam.append(sukrantxt)
        elif sukranhouse == "SIMMAM": rasisimmam.append(sukrantxt)
        elif sukranhouse == "KANNI": rasikanni.append(sukrantxt)
        elif sukranhouse == "THULAM": rasithulam.append(sukrantxt)
        elif sukranhouse == "VIRUCHIGAM": rasiviruchigam.append(sukrantxt)
        elif sukranhouse == "DHANUSU": rasidhanusu.append(sukrantxt)
        elif sukranhouse == "MAGARAM": rasimagaram.append(sukrantxt)
        elif sukranhouse == "KUMBAM": rasikumbam.append(sukrantxt)
        elif sukranhouse == "MEENAM": rasimeenam.append(sukrantxt)  
            
        if sevvaihouse == "MESHAM": rasimesham.append(sevvaitxt)
        elif sevvaihouse == "RISHABAM": rasirishabam.append(sevvaitxt)
        elif sevvaihouse == "MITHUNAM": rasimithunam.append(sevvaitxt)
        elif sevvaihouse == "KADAGAM": rasikadagam.append(sevvaitxt)
        elif sevvaihouse == "SIMMAM": rasisimmam.append(sevvaitxt)
        elif sevvaihouse == "KANNI": rasikanni.append(sevvaitxt)
        elif sevvaihouse == "THULAM": rasithulam.append(sevvaitxt)
        elif sevvaihouse == "VIRUCHIGAM": rasiviruchigam.append(sevvaitxt)
        elif sevvaihouse == "DHANUSU": rasidhanusu.append(sevvaitxt)
        elif sevvaihouse == "MAGARAM": rasimagaram.append(sevvaitxt)
        elif sevvaihouse == "KUMBAM": rasikumbam.append(sevvaitxt)
        elif sevvaihouse == "MEENAM": rasimeenam.append(sevvaitxt)              

        if guruhouse == "MESHAM": rasimesham.append(gurutxt)
        elif guruhouse == "RISHABAM": rasirishabam.append(gurutxt)
        elif guruhouse == "MITHUNAM": rasimithunam.append(gurutxt)
        elif guruhouse == "KADAGAM": rasikadagam.append(gurutxt)
        elif guruhouse == "SIMMAM": rasisimmam.append(gurutxt)
        elif guruhouse == "KANNI": rasikanni.append(gurutxt)
        elif guruhouse == "THULAM": rasithulam.append(gurutxt)
        elif guruhouse == "VIRUCHIGAM": rasiviruchigam.append(gurutxt)
        elif guruhouse == "DHANUSU": rasidhanusu.append(gurutxt)
        elif guruhouse == "MAGARAM": rasimagaram.append(gurutxt)
        elif guruhouse == "KUMBAM": rasikumbam.append(gurutxt)
        elif guruhouse == "MEENAM": rasimeenam.append(gurutxt)              

        if sanihouse == "MESHAM": rasimesham.append(sanitxt)
        elif sanihouse == "RISHABAM": rasirishabam.append(sanitxt)
        elif sanihouse == "MITHUNAM": rasimithunam.append(sanitxt)
        elif sanihouse == "KADAGAM": rasikadagam.append(sanitxt)
        elif sanihouse == "SIMMAM": rasisimmam.append(sanitxt)
        elif sanihouse == "KANNI": rasikanni.append(sanitxt)
        elif sanihouse == "THULAM": rasithulam.append(sanitxt)
        elif sanihouse == "VIRUCHIGAM": rasiviruchigam.append(sanitxt)
        elif sanihouse == "DHANUSU": rasidhanusu.append(sanitxt)
        elif sanihouse == "MAGARAM": rasimagaram.append(sanitxt)
        elif sanihouse == "KUMBAM": rasikumbam.append(sanitxt)
        elif sanihouse == "MEENAM": rasimeenam.append(sanitxt)      

        if raghuhouse == "MESHAM": rasimesham.append("ராகு")
        elif raghuhouse == "RISHABAM": rasirishabam.append("ராகு")
        elif raghuhouse == "MITHUNAM": rasimithunam.append("ராகு")
        elif raghuhouse == "KADAGAM": rasikadagam.append("ராகு")
        elif raghuhouse == "SIMMAM": rasisimmam.append("ராகு")
        elif raghuhouse == "KANNI": rasikanni.append("ராகு")
        elif raghuhouse == "THULAM": rasithulam.append("ராகு")
        elif raghuhouse == "VIRUCHIGAM": rasiviruchigam.append("ராகு")
        elif raghuhouse == "DHANUSU": rasidhanusu.append("ராகு")
        elif raghuhouse == "MAGARAM": rasimagaram.append("ராகு")
        elif raghuhouse == "KUMBAM": rasikumbam.append("ராகு")
        elif raghuhouse == "MEENAM": rasimeenam.append("ராகு")      

        if kethuhouse == "MESHAM": rasimesham.append("கேது")
        elif kethuhouse == "RISHABAM": rasirishabam.append("கேது")
        elif kethuhouse == "MITHUNAM": rasimithunam.append("கேது")
        elif kethuhouse == "KADAGAM": rasikadagam.append("கேது")
        elif kethuhouse == "SIMMAM": rasisimmam.append("கேது")
        elif kethuhouse == "KANNI": rasikanni.append("கேது")
        elif kethuhouse == "THULAM": rasithulam.append("கேது")
        elif kethuhouse == "VIRUCHIGAM": rasiviruchigam.append("கேது")
        elif kethuhouse == "DHANUSU": rasidhanusu.append("கேது")
        elif kethuhouse == "MAGARAM": rasimagaram.append("கேது")
        elif kethuhouse == "KUMBAM": rasikumbam.append("கேது")
        elif kethuhouse == "MEENAM": rasimeenam.append("கேது")      
        

        if lagnam_amsamhouse == "MESHAM": amsam_rasimesham.append("லக்")
        elif lagnam_amsamhouse == "RISHABAM": amsam_rasirishabam.append("லக்")
        elif lagnam_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("லக்")
        elif lagnam_amsamhouse == "KADAGAM": amsam_rasikadagam.append("லக்")
        elif lagnam_amsamhouse == "SIMMAM": amsam_rasisimmam.append("லக்")
        elif lagnam_amsamhouse == "KANNI": amsam_rasikanni.append("லக்")
        elif lagnam_amsamhouse == "THULAM": amsam_rasithulam.append("லக்")
        elif lagnam_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("லக்")
        elif lagnam_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("லக்")
        elif lagnam_amsamhouse == "MAGARAM": amsam_rasimagaram.append("லக்")
        elif lagnam_amsamhouse == "KUMBAM": amsam_rasikumbam.append("லக்")
        elif lagnam_amsamhouse == "MEENAM": amsam_rasimeenam.append("லக்")    


        if sun_amsamhouse == "MESHAM": amsam_rasimesham.append("சூரி")
        elif sun_amsamhouse == "RISHABAM": amsam_rasirishabam.append("சூரி")
        elif sun_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("சூரி")
        elif sun_amsamhouse == "KADAGAM": amsam_rasikadagam.append("சூரி")
        elif sun_amsamhouse == "SIMMAM": amsam_rasisimmam.append("சூரி")
        elif sun_amsamhouse == "KANNI": amsam_rasikanni.append("சூரி")
        elif sun_amsamhouse == "THULAM": amsam_rasithulam.append("சூரி")
        elif sun_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("சூரி")
        elif sun_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("சூரி")
        elif sun_amsamhouse == "MAGARAM": amsam_rasimagaram.append("சூரி")
        elif sun_amsamhouse == "KUMBAM": amsam_rasikumbam.append("சூரி")
        elif sun_amsamhouse == "MEENAM": amsam_rasimeenam.append("சூரி")        

        if moon_amsamhouse == "MESHAM": amsam_rasimesham.append("சந்")
        elif moon_amsamhouse == "RISHABAM": amsam_rasirishabam.append("சந்")
        elif moon_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("சந்")
        elif moon_amsamhouse == "KADAGAM": amsam_rasikadagam.append("சந்")
        elif moon_amsamhouse == "SIMMAM": amsam_rasisimmam.append("சந்")
        elif moon_amsamhouse == "KANNI": amsam_rasikanni.append("சந்")
        elif moon_amsamhouse == "THULAM": amsam_rasithulam.append("சந்")
        elif moon_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("சந்")
        elif moon_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("சந்")
        elif moon_amsamhouse == "MAGARAM": amsam_rasimagaram.append("சந்")
        elif moon_amsamhouse == "KUMBAM": amsam_rasikumbam.append("சந்")
        elif moon_amsamhouse == "MEENAM": amsam_rasimeenam.append("சந்")  

        if bhudhan_amsamhouse == "MESHAM": amsam_rasimesham.append(bhudhantxt)
        elif bhudhan_amsamhouse == "RISHABAM": amsam_rasirishabam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "KADAGAM": amsam_rasikadagam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "SIMMAM": amsam_rasisimmam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "KANNI": amsam_rasikanni.append(bhudhantxt)
        elif bhudhan_amsamhouse == "THULAM": amsam_rasithulam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(bhudhantxt)
        elif bhudhan_amsamhouse == "MAGARAM": amsam_rasimagaram.append(bhudhantxt)
        elif bhudhan_amsamhouse == "KUMBAM": amsam_rasikumbam.append(bhudhantxt)
        elif bhudhan_amsamhouse == "MEENAM": amsam_rasimeenam.append(bhudhantxt)  

        if sukran_amsamhouse == "MESHAM": amsam_rasimesham.append(sukrantxt)
        elif sukran_amsamhouse == "RISHABAM": amsam_rasirishabam.append(sukrantxt)
        elif sukran_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(sukrantxt)
        elif sukran_amsamhouse == "KADAGAM": amsam_rasikadagam.append(sukrantxt)
        elif sukran_amsamhouse == "SIMMAM": amsam_rasisimmam.append(sukrantxt)
        elif sukran_amsamhouse == "KANNI": amsam_rasikanni.append(sukrantxt)
        elif sukran_amsamhouse == "THULAM": amsam_rasithulam.append(sukrantxt)
        elif sukran_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(sukrantxt)
        elif sukran_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(sukrantxt)
        elif sukran_amsamhouse == "MAGARAM": amsam_rasimagaram.append(sukrantxt)
        elif sukran_amsamhouse == "KUMBAM": amsam_rasikumbam.append(sukrantxt)
        elif sukran_amsamhouse == "MEENAM": amsam_rasimeenam.append(sukrantxt)  
            
        if sevvai_amsamhouse == "MESHAM": amsam_rasimesham.append(sevvaitxt)
        elif sevvai_amsamhouse == "RISHABAM": amsam_rasirishabam.append(sevvaitxt)
        elif sevvai_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(sevvaitxt)
        elif sevvai_amsamhouse == "KADAGAM": amsam_rasikadagam.append(sevvaitxt)
        elif sevvai_amsamhouse == "SIMMAM": amsam_rasisimmam.append(sevvaitxt)
        elif sevvai_amsamhouse == "KANNI": amsam_rasikanni.append(sevvaitxt)
        elif sevvai_amsamhouse == "THULAM": amsam_rasithulam.append(sevvaitxt)
        elif sevvai_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(sevvaitxt)
        elif sevvai_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(sevvaitxt)
        elif sevvai_amsamhouse == "MAGARAM": amsam_rasimagaram.append(sevvaitxt)
        elif sevvai_amsamhouse == "KUMBAM": amsam_rasikumbam.append(sevvaitxt)
        elif sevvai_amsamhouse == "MEENAM": amsam_rasimeenam.append(sevvaitxt)              

        if guru_amsamhouse == "MESHAM": amsam_rasimesham.append(gurutxt)
        elif guru_amsamhouse == "RISHABAM": amsam_rasirishabam.append(gurutxt)
        elif guru_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(gurutxt)
        elif guru_amsamhouse == "KADAGAM": amsam_rasikadagam.append(gurutxt)
        elif guru_amsamhouse == "SIMMAM": amsam_rasisimmam.append(gurutxt)
        elif guru_amsamhouse == "KANNI": amsam_rasikanni.append(gurutxt)
        elif guru_amsamhouse == "THULAM": amsam_rasithulam.append(gurutxt)
        elif guru_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(gurutxt)
        elif guru_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(gurutxt)
        elif guru_amsamhouse == "MAGARAM": amsam_rasimagaram.append(gurutxt)
        elif guru_amsamhouse == "KUMBAM": amsam_rasikumbam.append(gurutxt)
        elif guru_amsamhouse == "MEENAM": amsam_rasimeenam.append(gurutxt)              

        if sani_amsamhouse == "MESHAM": amsam_rasimesham.append(sanitxt)
        elif sani_amsamhouse == "RISHABAM": amsam_rasirishabam.append(sanitxt)
        elif sani_amsamhouse == "MITHUNAM": amsam_rasimithunam.append(sanitxt)
        elif sani_amsamhouse == "KADAGAM": amsam_rasikadagam.append(sanitxt)
        elif sani_amsamhouse == "SIMMAM": amsam_rasisimmam.append(sanitxt)
        elif sani_amsamhouse == "KANNI": amsam_rasikanni.append(sanitxt)
        elif sani_amsamhouse == "THULAM": amsam_rasithulam.append(sanitxt)
        elif sani_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append(sanitxt)
        elif sani_amsamhouse == "DHANUSU": amsam_rasidhanusu.append(sanitxt)
        elif sani_amsamhouse == "MAGARAM": amsam_rasimagaram.append(sanitxt)
        elif sani_amsamhouse == "KUMBAM": amsam_rasikumbam.append(sanitxt)
        elif sani_amsamhouse == "MEENAM": amsam_rasimeenam.append(sanitxt)      

        if raghu_amsamhouse == "MESHAM": amsam_rasimesham.append("ராகு")
        elif raghu_amsamhouse == "RISHABAM": amsam_rasirishabam.append("ராகு")
        elif raghu_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("ராகு")
        elif raghu_amsamhouse == "KADAGAM": amsam_rasikadagam.append("ராகு")
        elif raghu_amsamhouse == "SIMMAM": amsam_rasisimmam.append("ராகு")
        elif raghu_amsamhouse == "KANNI": amsam_rasikanni.append("ராகு")
        elif raghu_amsamhouse == "THULAM": amsam_rasithulam.append("ராகு")
        elif raghu_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("ராகு")
        elif raghu_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("ராகு")
        elif raghu_amsamhouse == "MAGARAM": amsam_rasimagaram.append("ராகு")
        elif raghu_amsamhouse == "KUMBAM": amsam_rasikumbam.append("ராகு")
        elif raghu_amsamhouse == "MEENAM": amsam_rasimeenam.append("ராகு")      

        if kethu_amsamhouse == "MESHAM": amsam_rasimesham.append("கேது")
        elif kethu_amsamhouse == "RISHABAM": amsam_rasirishabam.append("கேது")
        elif kethu_amsamhouse == "MITHUNAM": amsam_rasimithunam.append("கேது")
        elif kethu_amsamhouse == "KADAGAM": amsam_rasikadagam.append("கேது")
        elif kethu_amsamhouse == "SIMMAM": amsam_rasisimmam.append("கேது")
        elif kethu_amsamhouse == "KANNI": amsam_rasikanni.append("கேது")
        elif kethu_amsamhouse == "THULAM": amsam_rasithulam.append("கேது")
        elif kethu_amsamhouse == "VIRUCHIGAM": amsam_rasiviruchigam.append("கேது")
        elif kethu_amsamhouse == "DHANUSU": amsam_rasidhanusu.append("கேது")
        elif kethu_amsamhouse == "MAGARAM": amsam_rasimagaram.append("கேது")
        elif kethu_amsamhouse == "KUMBAM": amsam_rasikumbam.append("கேது")
        elif kethu_amsamhouse == "MEENAM": amsam_rasimeenam.append("கேது")              

        rasivalues_global = []
        rasivalues_global.append((hora.p1_format(rasimesham)))
        rasivalues_global.append((hora.p1_format(rasirishabam)))
        rasivalues_global.append((hora.p1_format(rasimithunam)))
        rasivalues_global.append((hora.p1_format(rasikadagam)))
        rasivalues_global.append((hora.p1_format(rasisimmam)))
        rasivalues_global.append((hora.p1_format(rasikanni)))
        rasivalues_global.append((hora.p1_format(rasithulam)))
        rasivalues_global.append((hora.p1_format(rasiviruchigam)))
        rasivalues_global.append((hora.p1_format(rasidhanusu)))
        rasivalues_global.append((hora.p1_format(rasimagaram)))
        rasivalues_global.append((hora.p1_format(rasikumbam)))
        rasivalues_global.append((hora.p1_format(rasimeenam)))
        

        amsamvalues_global = []
        amsamvalues_global.append(hora.p1_format(amsam_rasimesham))
        amsamvalues_global.append(hora.p1_format(amsam_rasirishabam))
        amsamvalues_global.append(hora.p1_format(amsam_rasimithunam))
        amsamvalues_global.append(hora.p1_format(amsam_rasikadagam))
        amsamvalues_global.append(hora.p1_format(amsam_rasisimmam))
        amsamvalues_global.append(hora.p1_format(amsam_rasikanni))
        amsamvalues_global.append(hora.p1_format(amsam_rasithulam))
        amsamvalues_global.append(hora.p1_format(amsam_rasiviruchigam))
        amsamvalues_global.append(hora.p1_format(amsam_rasidhanusu))
        amsamvalues_global.append(hora.p1_format(amsam_rasimagaram))
        amsamvalues_global.append(hora.p1_format(amsam_rasikumbam))
        amsamvalues_global.append(hora.p1_format(amsam_rasimeenam))
        
        #print (rasivalues_global)
        
        #print(rasimesham)
        #print(rasirishabam)
        #print(rasimithunam)
        #print(rasikadagam)
        #print(rasisimmam)
        #print(rasikanni)
        #print(rasithulam)
        #print(rasiviruchigam)
        #print(rasidhanusu)
        #print(rasimagaram)    
        #print(rasikumbam)
        #print(rasimeenam)
        #print("  ")
        
        fnt = QFont('Catamaran', 12)
        fnta = QFont('Arial', 12)
        
        self.rasi_mesham_lbl.setFont(fnt);
        self.rasi_rishabam_lbl.setFont(fnt);
        self.rasi_mithunam_lbl.setFont(fnt);
        self.rasi_kadagam_lbl.setFont(fnt);
        self.rasi_simmam_lbl.setFont(fnt);
        self.rasi_kanni_lbl.setFont(fnt);
        self.rasi_thulam_lbl.setFont(fnt);
        self.rasi_viruchigam_lbl.setFont(fnt);
        self.rasi_dhanusu_lbl.setFont(fnt);
        self.rasi_magaram_lbl.setFont(fnt);
        self.rasi_kumbam_lbl.setFont(fnt);
        self.rasi_meenam_lbl.setFont(fnt);
        self.rasi_center_lbl.setFont(fnta);
                
        
        self.rasi_mesham_lbl.setText(hora.p_format(rasimesham))
        self.rasi_rishabam_lbl.setText(hora.p_format(rasirishabam))
        self.rasi_mithunam_lbl.setText(hora.p_format(rasimithunam))
        self.rasi_kadagam_lbl.setText(hora.p_format(rasikadagam))
        self.rasi_simmam_lbl.setText(hora.p_format(rasisimmam))
        self.rasi_kanni_lbl.setText(hora.p_format(rasikanni))
        self.rasi_thulam_lbl.setText(hora.p_format(rasithulam))
        self.rasi_viruchigam_lbl.setText(hora.p_format(rasiviruchigam))
        self.rasi_dhanusu_lbl.setText(hora.p_format(rasidhanusu))
        self.rasi_magaram_lbl.setText(hora.p_format(rasimagaram))
        self.rasi_kumbam_lbl.setText(hora.p_format(rasikumbam))
        self.rasi_meenam_lbl.setText(hora.p_format(rasimeenam))
        self.rasi_center_lbl.setText("ராசி")       
        

        self.amsam_mesham_lbl.setFont(fnt);
        self.amsam_rishabam_lbl.setFont(fnt);
        self.amsam_mithunam_lbl.setFont(fnt);
        self.amsam_kadagam_lbl.setFont(fnt);
        self.amsam_simmam_lbl.setFont(fnt);
        self.amsam_kanni_lbl.setFont(fnt);
        self.amsam_thulam_lbl.setFont(fnt);
        self.amsam_viruchigam_lbl.setFont(fnt);
        self.amsam_dhanusu_lbl.setFont(fnt);
        self.amsam_magaram_lbl.setFont(fnt);
        self.amsam_kumbam_lbl.setFont(fnt);
        self.amsam_meenam_lbl.setFont(fnt);
        self.amsam_center_lbl.setFont(fnta);    
        
        self.amsam_mesham_lbl.setText(hora.p_format(amsam_rasimesham))
        self.amsam_rishabam_lbl.setText(hora.p_format(amsam_rasirishabam))
        self.amsam_mithunam_lbl.setText(hora.p_format(amsam_rasimithunam))
        self.amsam_kadagam_lbl.setText(hora.p_format(amsam_rasikadagam))
        self.amsam_simmam_lbl.setText(hora.p_format(amsam_rasisimmam))
        self.amsam_kanni_lbl.setText(hora.p_format(amsam_rasikanni))
        self.amsam_thulam_lbl.setText(hora.p_format(amsam_rasithulam))
        self.amsam_viruchigam_lbl.setText(hora.p_format(amsam_rasiviruchigam))
        self.amsam_dhanusu_lbl.setText(hora.p_format(amsam_rasidhanusu))
        self.amsam_magaram_lbl.setText(hora.p_format(amsam_rasimagaram))
        self.amsam_kumbam_lbl.setText(hora.p_format(amsam_rasikumbam))
        self.amsam_meenam_lbl.setText(hora.p_format(amsam_rasimeenam))
        self.amsam_center_lbl.setText("நவாம்சம்")

        fnt = QFont('Catamaran', 12)
            
        self.tableWidget.setRowCount(0);
        self.tableWidget.setColumnCount(0);
        self.tableWidget.setRowCount(10);
        self.tableWidget.setColumnCount(5);

        self.tableWidget.setFont(fnt);
        
        self.tableWidget.horizontalHeader().setFont(fnt)
        self.tableWidget.verticalHeader().setFont(fnt)
        
        self.tableWidget.setHorizontalHeaderLabels(['ராசி','ராசி டிகிரி','நட்சத்திரம் ','நட்ச. அதிபதி','தீர்காம்சம்'])
        self.tableWidget.setVerticalHeaderLabels(['லக்னம்','சூரியன்','சந்திரன்','புதன்','சுக்ரன்','செவ்வாய்','குரு ','சனி','ராகு','கேது'])

        #header = self.tableWidget.horizontalHeader()       
        #header.setSectionResizeMode(0, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(1, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(2, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(3, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(4, qtw.QHeaderView.Stretch)
        #header.setSectionResizeMode(5, qtw.QHeaderView.Stretch)
        #self.tableWidget.setColumnWidth(0, 60)        
        #self.tableWidget.setColumnWidth(1, 60)
        #self.tableWidget.setColumnWidth(3, 20)

      
        self.tableWidget.setItem(0,0, QTableWidgetItem(lagnamhouse_tamil)) 
        self.tableWidget.setItem(1,0, QTableWidgetItem(sunhouse_tamil))         
        self.tableWidget.setItem(2,0, QTableWidgetItem(moonhouse_tamil))         
        self.tableWidget.setItem(3,0, QTableWidgetItem(bhudhanhouse_tamil))         
        self.tableWidget.setItem(4,0, QTableWidgetItem(sukranhouse_tamil))         
        self.tableWidget.setItem(5,0, QTableWidgetItem(sevvaihouse_tamil))         
        self.tableWidget.setItem(6,0, QTableWidgetItem(guruhouse_tamil))  
        self.tableWidget.setItem(7,0, QTableWidgetItem(sanihouse_tamil))         
        self.tableWidget.setItem(8,0, QTableWidgetItem(raghuhouse_tamil))         
        self.tableWidget.setItem(9,0, QTableWidgetItem(kethuhouse_tamil))        


        self.tableWidget.setItem(0,1, QTableWidgetItem(lagnamdegree)) 
        self.tableWidget.setItem(1,1, QTableWidgetItem(sundegree))         
        self.tableWidget.setItem(2,1, QTableWidgetItem(moondegree))         
        self.tableWidget.setItem(3,1, QTableWidgetItem(bhudhandegree))         
        self.tableWidget.setItem(4,1, QTableWidgetItem(sukrandegree))         
        self.tableWidget.setItem(5,1, QTableWidgetItem(sevvaidegree))         
        self.tableWidget.setItem(6,1, QTableWidgetItem(gurudegree))  
        self.tableWidget.setItem(7,1, QTableWidgetItem(sanidegree))         
        self.tableWidget.setItem(8,1, QTableWidgetItem(raghudegree))         
        self.tableWidget.setItem(9,1, QTableWidgetItem(kethudegree))      

        lagnamstarpadam = lagnamstar_tamil + " - " + str(hora.star_padam(float(lagnamlat)))
        sunstarpadam = sunstar_tamil + " - " + str(hora.star_padam(float(sunlat)))
        moonstarpadam = moonstar_tamil + " - " + str(hora.star_padam(float(moonlat)))
        bhudhanstarpadam = bhudhanstar_tamil + " - " + str(hora.star_padam(float(bhudhanlat)))
        sukranstarpadam = sukranstar_tamil + " - " + str(hora.star_padam(float(sukranlat)))
        sevvaistarpadam = sevvaistar_tamil + " - " + str(hora.star_padam(float(sevvailat)))
        gurustarpadam = gurustar_tamil + " - " + str(hora.star_padam(float(gurulat)))
        sanistarpadam = sanistar_tamil + " - " + str(hora.star_padam(float(sanilat)))
        raghustarpadam = raghustar_tamil + " - " + str(hora.star_padam(float(raghulat)))
        kethustarpadam = kethustar_tamil + " - " + str(hora.star_padam(float(kethulat)))
        
        self.tableWidget.setItem(0,2, QTableWidgetItem(lagnamstarpadam)) 
        self.tableWidget.setItem(1,2, QTableWidgetItem(sunstarpadam))         
        self.tableWidget.setItem(2,2, QTableWidgetItem(moonstarpadam))         
        self.tableWidget.setItem(3,2, QTableWidgetItem(bhudhanstarpadam))         
        self.tableWidget.setItem(4,2, QTableWidgetItem(sukranstarpadam))         
        self.tableWidget.setItem(5,2, QTableWidgetItem(sevvaistarpadam))         
        self.tableWidget.setItem(6,2, QTableWidgetItem(gurustarpadam))  
        self.tableWidget.setItem(7,2, QTableWidgetItem(sanistarpadam))         
        self.tableWidget.setItem(8,2, QTableWidgetItem(raghustarpadam))         
        self.tableWidget.setItem(9,2, QTableWidgetItem(kethustarpadam))      


        self.tableWidget.setItem(0,3, QTableWidgetItem(hora.star_lord_tamil(float(lagnamlat))))
        self.tableWidget.setItem(1,3, QTableWidgetItem(hora.star_lord_tamil(float(sunlat))))         
        self.tableWidget.setItem(2,3, QTableWidgetItem(hora.star_lord_tamil(float(moonlat))))         
        self.tableWidget.setItem(3,3, QTableWidgetItem(hora.star_lord_tamil(float(bhudhanlat))))        
        self.tableWidget.setItem(4,3, QTableWidgetItem(hora.star_lord_tamil(float(sukranlat))))         
        self.tableWidget.setItem(5,3, QTableWidgetItem(hora.star_lord_tamil(float(sevvailat))))         
        self.tableWidget.setItem(6,3, QTableWidgetItem(hora.star_lord_tamil(float(gurulat))))  
        self.tableWidget.setItem(7,3, QTableWidgetItem(hora.star_lord_tamil(float(sanilat))))         
        self.tableWidget.setItem(8,3, QTableWidgetItem(hora.star_lord_tamil(float(raghulat))))         
        self.tableWidget.setItem(9,3, QTableWidgetItem(hora.star_lord_tamil(float(kethulat))))

        
        self.tableWidget.setItem(0,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(lagnamlat))))
        self.tableWidget.setItem(1,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(sunlat))))         
        self.tableWidget.setItem(2,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(moonlat))))         
        self.tableWidget.setItem(3,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(bhudhanlat))))        
        self.tableWidget.setItem(4,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(sukranlat))))         
        self.tableWidget.setItem(5,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(sevvailat))))         
        self.tableWidget.setItem(6,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(gurulat))))  
        self.tableWidget.setItem(7,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(sanilat))))         
        self.tableWidget.setItem(8,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(raghulat))))         
        self.tableWidget.setItem(9,4, QTableWidgetItem(hora.Convert_Longitude_into_time(float(kethulat))))

        native_name = self.lineEdit_Nativename.text()
        native_sex = self.comboBox_Sex.currentText()
        native_date = self.dateEdit_Dob.date()
        native_time = self.timeEdit_Btime.time()
        native_day = native_date.day()
        native_month = native_date.month()
        native_year = native_date.year()
        native_hour = native_time.toString("hh")
        native_minutes = native_time.toString("mm")
        native_seconds = native_time.toString("ss")
        native_birthplace = self.lineEdit_Birthplace.text()
        native_timezone = self.comboBox_Timezone.currentText()
        native_longdeg = self.lineEdit_Longitudedeg.text()
        native_longdir = self.comboBox_Longitudedir.currentText()
        native_longmin = self.lineEdit_Longitudemin.text()
        native_latdeg = self.lineEdit_Lattitudedeg.text()
        native_latdir = self.comboBox_Lattitudedir.currentText()
        native_latmin = self.lineEdit_Lattitudemin.text()
        native_language = self.comboBox_Language.currentText()
        tp_date = str(native_day) + "/" + str(native_month) + "/" + str(native_year)  
        tp_time_print = native_hour + ":" + native_minutes + ":" + native_seconds    
        native_birth_array = native_birthplace.split("-")        
        native_birthplace_1 = native_birth_array[0]
        
        if native_name=="":
            native_name="தற்போதைய கோச்சாரம்"

        native_text = "<h4>ஜாதகர் தகவல்கள்</h4><table><tr><td>பெயர் : </td><td>" + native_name + "</td></tr><tr><td>பாலினம் : </td><td>" + self.comboBox_Sex.currentText() + "</td></tr><tr><td>பிறந்த தேதி : </td><td>" + tp_date + "</td></tr><tr><td>பிறந்த நேரம் : </td><td>" + native_hour + ":" + native_minutes + ":" + native_seconds + "</td></tr><tr><td>பிறந்த இடம் : </td><td>" + self.lineEdit_Birthplace.text() + "</td></tr></table>"
        
        txt=""
        thithi = hora.find_thithi(moonlat, sunlat,"tamil")
        yoga = hora.find_yoga(moonlat, sunlat,"tamil")
        karnam = hora.find_karnam(moonlat, sunlat,"tamil")
        
        dateobj = datetime.date(native_year, native_month, native_day)

        dasavalues = self.dasabhukthitree(float(moonlat),tp_date,"tamil")
        
        dasavalues = "<table><tr><td width=100%>" + dasavalues + "</td></tr></table>"        
        
        panjangam_text = "<h4>பஞ்சாங்கம் </h4><table><tr><td>லக்கினம்: </td><td>" + lagnamhouse_tamil + "</td></tr><tr><td>ராசி : </td><td>" + moonhouse_tamil + "</td></tr><tr><td>நட்சத்திரம்: </td><td>" + moonstar_tamil + "</td></tr><tr><td>திதி: </td><td>" + thithi + "</td></tr><tr><td>கர்ணம்: </td><td>" + karnam + "</td></tr><tr><td>யோகம்: </td><td>" + yoga + "</td></tr><tr><td>கிழமை: </td><td>" + hora.tamilday(dateobj.strftime('%A')) + "</td></tr></table>"
        
        panjangam_text = panjangam_text + "<br>" + dasavalues
        
        print_head = self.lineEdit_Nativename.text()
        if print_head=="":
            print_head = "கோச்சார ஜாதகம்"
        else:
            print_head = print_head + ""
        
           
        
        self.label_panjangam.setFont(fnt)
        self.label_dasa.setFont(fnt)
        
        self.label_panjangam.setText(native_text)
        self.label_dasa.setText(panjangam_text) 


        nameletters = hora.nameletterstamil(hora.star_query(float(moonlat)))
        startrees = hora.startreestamil(hora.star_query(float(moonlat)))

        
        print_essentials = []
        print_essentials.append(print_head)
        print_essentials.append(native_sex)
        print_essentials.append(tp_date)        
        print_essentials.append(tp_time_print)        
        print_essentials.append(native_birthplace_1)
        print_essentials.append(lagnamhouse_tamil)
        print_essentials.append(moonhouse_tamil)        
        print_essentials.append(moonstar_tamil)     
        print_essentials.append(thithi)    
        print_essentials.append(karnam)            
        print_essentials.append(yoga)
        print_essentials.append(hora.tamilday(dateobj.strftime('%A')))        
        print_essentials.append(dasavalues)
        print_essentials.append(nameletters)
        print_essentials.append(startrees)
        
        planettable_html = "<table><tr><th width='16%'>கிரகம்</th><th width='16%'>தீர்காம்சம்</th><th width='15%'>ராசி</th><th width='13%'>டிகிரி</th><th width='22%'>நட்சத்திரம்</th><th width='18%'>நட்ச. அதிபதி</th></tr><tr><td>" + "லக்னம்" + "</td><td>" + hora.Convert_Longitude_into_time(float(lagnamlat)) + "</td><td>" + lagnamhouse_tamil +"</td><td>" + lagnamdegree +"</td><td>" + lagnamstarpadam +"</td><td>" + hora.star_lord_tamil(float(lagnamlat)) +"</td></tr><tr><td>" + 'சூரியன்' + "</td><td>"+hora.Convert_Longitude_into_time(float(sunlat))+"</td><td>"+sunhouse_tamil+"</td><td>"+sundegree+"</td><td>"+sunstarpadam+"</td><td>" + hora.star_lord_tamil(float(sunlat)) +"</td></tr><tr><td>"+ 'சந்திரன்' +"</td><td>"+hora.Convert_Longitude_into_time(float(moonlat))+"</td><td>"+moonhouse_tamil+"</td><td>"+moondegree+"</td><td>"+moonstarpadam+"</td><td>" + hora.star_lord_tamil(float(moonlat)) +"</td></tr><tr><td>" +'புதன்' + "</td><td>"+hora.Convert_Longitude_into_time(float(bhudhanlat))+"</td><td>"+bhudhanhouse_tamil+"</td><td>"+bhudhandegree+"</td><td>"+bhudhanstarpadam+"</td><td>" + hora.star_lord_tamil(float(bhudhanlat)) +"</td></tr><tr><td>"+ 'சுக்ரன்' +"</td><td>"+hora.Convert_Longitude_into_time(float(sukranlat))+"</td><td>"+sukranhouse_tamil+"</td><td>"+sukrandegree+"</td><td>"+sukranstarpadam+"</td><td>" + hora.star_lord_tamil(float(sukranlat)) +"</td></tr><tr><td>" + 'செவ்வாய்' +"</td><td>"+hora.Convert_Longitude_into_time(float(sevvailat))+"</td><td>"+sevvaihouse_tamil+"</td><td>"+sevvaidegree+"</td><td>"+sevvaistarpadam+"</td><td>" + hora.star_lord_tamil(float(sevvailat)) +"</td></tr><tr><td>"+ 'குரு' +"</td><td>"+hora.Convert_Longitude_into_time(float(gurulat))+"</td><td>"+guruhouse_tamil+"</td><td>"+gurudegree+"</td><td>"+gurustarpadam+"</td><td>" + hora.star_lord_tamil(float(gurulat)) +"</td></tr><tr><td>"+'சனி' +"</td><td>"+hora.Convert_Longitude_into_time(float(sanilat))+"</td><td>"+sanihouse_tamil+"</td><td>"+sanidegree+"</td><td>"+sanistarpadam+"</td><td>" + hora.star_lord_tamil(float(sanilat)) +"</td></tr><tr><td>"+'ராகு' +"</td><td>"+hora.Convert_Longitude_into_time(float(raghulat))+"</td><td>"+raghuhouse_tamil+"</td><td>"+raghudegree+"</td><td>"+raghustarpadam+"</td><td>" + hora.star_lord_tamil(float(raghulat)) +"</td></tr><tr><td>"+'கேது' +"</td><td>"+hora.Convert_Longitude_into_time(float(kethulat))+"</td><td>"+kethuhouse_tamil+"</td><td>"+kethudegree+"</td><td>"+kethustarpadam+"</td><td>" + hora.star_lord_tamil(float(kethulat)) +"</td></tr></table>"

        self.preview.build_horoscope("tamil",rasivalues_global,amsamvalues_global,planettable_html, print_essentials)
        

   
    def dasatree(self):
        self.treeView_dasa.setHeaderHidden(True)
        
        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()   

        # America
        america = StandardItem('America', 16, set_bold=True)
     
        california = StandardItem('California', 14)
        america.appendRow(california)
     
        oakland = StandardItem('Oakland', 12, color=QColor(155, 0, 0))
        sanfrancisco = StandardItem('San Francisco', 12, color=QColor(155, 0, 0))
        sanjose = StandardItem('San Jose', 12, color=QColor(155, 0, 0))
     
        california.appendRow(oakland)
        california.appendRow(sanfrancisco)
        california.appendRow(sanjose)
        
        texas = StandardItem('Texas', 14)
        america.appendRow(texas)
     
        austin = StandardItem('Austin', 12, color=QColor(155, 0, 0))
        houston = StandardItem('Houston', 12, color=QColor(155, 0, 0))
        dallas = StandardItem('dallas', 12, color=QColor(155, 0, 0))
     
        texas.appendRow(austin)
        texas.appendRow(houston)
        texas.appendRow(dallas)
     
     
        # Canada 
        canada = StandardItem('America', 16, set_bold=True)
     
        alberta = StandardItem('Alberta', 14)
        bc = StandardItem('British Columbia', 14)
        ontario = StandardItem('Ontario', 14)
        canada.appendRows([alberta, bc, ontario])
     
        rootNode.appendRow(america)
        rootNode.appendRow(canada)
     
        self.treeView_dasa.setModel(treeModel)
        self.treeView_dasa.expandAll()
    
    
    def dasabhukthitree(self, moonlat, birthdate, language):

        self.treeView_dasa.setHeaderHidden(True)
    
        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()   
    
        star = hora.star_query(moonlat)
        starloard = hora.star_lord(moonlat)
        diffrence = (moonlat - hora.star_start_degree(star)) / 13.333333333333334
        starloarddasa = hora.starlorddasa(star)
        consumeddasayear = diffrence * starloarddasa;
        tdec = math.floor(consumeddasayear)
        tdec1 = consumeddasayear - tdec
        consumedmonths = tdec1 * 12
        tdec2 = math.floor(consumedmonths)
        tdec3 = consumedmonths - tdec2
        consumeddays = (tdec3 * 365.25) / 12
        tdec4 = math.floor(consumeddays)
        starlordtamil = hora.star_lord_tamil(moonlat)
        
        consumedperiod=""
        
        tdec5 = (tdec * 365.25) + (tdec2 * 30) + tdec4
        tdec6 = starloarddasa * 365.25
        tdec7 = tdec6 - tdec5
        totalconsumeddays = (tdec * 365.25) + (tdec2 * 30) + tdec4
        tdec8 = tdec7 / 365.25
        tdec9 = math.floor(tdec8)
        tdec10 = (tdec8 - tdec9) * 12
        tdec11 = math.floor(tdec10)
        tdec12 = tdec10 - tdec11
        tdec13 = (tdec12 * 365.25) / 12
        tdec14 = math.floor(tdec13)
        
        if language=="english":
            fnt = QFont('Arial', 12)
            consumedperiod = "(Balance Dasa " + str(tdec9) + " years " + str(tdec11) + " months " + str(tdec14) + " days)"
            consumedperiod_dasa = "Birth Dasa: " + hora.star_lord(moonlat) + " - Balance Dasa " + str(tdec9) + " years " + str(tdec11) + " months " + str(tdec14) + " days"
        elif language=="tamil":     
            fnt = QFont('Catamaran', 12)                
            consumedperiod = "(தசா இருப்பு   " + str(tdec9) + " வருடங்கள்  " + str(tdec11) + " மாதங்கள் " + str(tdec14) + " நாட்கள்)"  
            consumedperiod_dasa = "பிறப்பு தசா : " + starlordtamil + " - தசா இருப்பு   " + str(tdec9) + " வருடங்கள்  " + str(tdec11) + " மாதங்கள் " + str(tdec14) + " நாட்கள்"  

        kethu_planets_vimsottari_order_tamil = ["0","கேது","சுக்","சூரி","சந்","செவ்","ராகு","குரு","சனி","புத"]
        kethu_planets_vimsottari_order = ["0","Ke","Ve","Su","Mo","Ma","Ra","Ju","Sa","Me"]
        kethu_planets_vimsottari_dasayears = ["0","7","20","6","10","7","18","16","19","17"]

        venus_planets_vimsottari_order_tamil = ["0","சுக்","சூரி","சந்","செவ்","ராகு","குரு","சனி","புத","கேது"]
        venus_planets_vimsottari_order = ["0","Ve","Su","Mo","Ma","Ra","Ju","Sa","Me","Ke"]
        venus_planets_vimsottari_dasayears = ["0","20","6","10","7","18","16","19","17","7"]

        sun_planets_vimsottari_order_tamil = ["0","சூரி","சந்","செவ்","ராகு","குரு","சனி","புத","கேது","சுக்"]
        sun_planets_vimsottari_order = ["0","Su","Mo","Ma","Ra","Ju","Sa","Me","Ke","Ve"]
        sun_planets_vimsottari_dasayears = ["0","6","10","7","18","16","19","17","7","20"]
        
        moon_planets_vimsottari_order_tamil = ["0","சந்","செவ்","ராகு","குரு","சனி","புத","கேது","சுக்","சூரி"]
        moon_planets_vimsottari_order = ["0","Mo","Ma","Ra","Ju","Sa","Me","Ke","Ve","Su"]
        moon_planets_vimsottari_dasayears = ["0","10","7","18","16","19","17","7","20","6"]

        mars_planets_vimsottari_order_tamil = ["0","செவ்","ராகு","குரு","சனி","புத","கேது","சுக்","சூரி","சந்"]
        mars_planets_vimsottari_order = ["0","Ma","Ra","Ju","Sa","Me","Ke","Ve","Su","Mo"]
        mars_planets_vimsottari_dasayears = ["0","7","18","16","19","17","7","20","6","10"]

        raghu_planets_vimsottari_order_tamil = ["0","ராகு","குரு","சனி","புத","கேது","சுக்","சூரி","சந்","செவ்"]
        raghu_planets_vimsottari_order = ["0","Ra","Ju","Sa","Me","Ke","Ve","Su","Mo","Ma"]
        raghu_planets_vimsottari_dasayears = ["0","18","16","19","17","7","20","6","10","7"]

        guru_planets_vimsottari_order_tamil = ["0","குரு","சனி","புத","கேது","சுக்","சூரி","சந்","செவ்","ராகு"]
        guru_planets_vimsottari_order = ["0","Ju","Sa","Me","Ke","Ve","Su","Mo","Ma","Ra"]
        guru_planets_vimsottari_dasayears = ["0","16","19","17","7","20","6","10","7","18"]

        sani_planets_vimsottari_order_tamil = ["0","சனி","புத","கேது","சுக்","சூரி","சந்","செவ்","ராகு","குரு"]
        sani_planets_vimsottari_order = ["0","Sa","Me","Ke","Ve","Su","Mo","Ma","Ra","Ju"]
        sani_planets_vimsottari_dasayears = ["0","19","17","7","20","6","10","7","18","16"]

        bhudhan_planets_vimsottari_order_tamil = ["0","புத","கேது","சுக்","சூரி","சந்","செவ்","ராகு","குரு","சனி"]
        bhudhan_planets_vimsottari_order = ["0","Me","Ke","Ve","Su","Mo","Ma","Ra","Ju","Sa"]
        bhudhan_planets_vimsottari_dasayears = ["0","17","7","20","6","10","7","18","16","19"]

        if starloard == "Kethu":
            if language=="english":
                pname = kethu_planets_vimsottari_order
            elif language=="tamil":
                pname = kethu_planets_vimsottari_order_tamil
            v_dasa = kethu_planets_vimsottari_dasayears
        elif starloard == "Venus":
            if language=="english":
                pname = venus_planets_vimsottari_order
            elif language=="tamil":
                pname = venus_planets_vimsottari_order_tamil
            v_dasa = venus_planets_vimsottari_dasayears
        elif starloard == "Sun":
            if language=="english":
                pname = sun_planets_vimsottari_order
            elif language=="tamil":
                pname = sun_planets_vimsottari_order_tamil
            v_dasa = sun_planets_vimsottari_dasayears    
        elif starloard == "Moon":
            if language=="english":
                pname = moon_planets_vimsottari_order
            elif language=="tamil":    
                pname = moon_planets_vimsottari_order_tamil
            v_dasa = moon_planets_vimsottari_dasayears    
        elif starloard == "Mars":
            if language=="english":
                pname = mars_planets_vimsottari_order
            elif language=="tamil":    
                pname = mars_planets_vimsottari_order_tamil
            v_dasa = mars_planets_vimsottari_dasayears    
        elif starloard == "Raghu":
            if language=="english":
                pname = raghu_planets_vimsottari_order
            elif language=="tamil":    
                pname = raghu_planets_vimsottari_order_tamil
            v_dasa = raghu_planets_vimsottari_dasayears    
        elif starloard == "Jupiter":
            if language=="english":
                pname = guru_planets_vimsottari_order
            elif language=="tamil":    
                pname = guru_planets_vimsottari_order_tamil
            v_dasa = guru_planets_vimsottari_dasayears        
        elif starloard == "Saturn":
            if language=="english":
                pname = sani_planets_vimsottari_order
            elif language=="tamil":    
                pname = sani_planets_vimsottari_order_tamil
            v_dasa = sani_planets_vimsottari_dasayears        
        elif starloard == "Mercury":
            if language=="english":
                pname = bhudhan_planets_vimsottari_order
            elif language=="tamil":    
                pname = bhudhan_planets_vimsottari_order_tamil
            v_dasa = bhudhan_planets_vimsottari_dasayears                                        


        
        idasaLord = 0
        ibhuktiLord = 0
        iantraLord = 0
        SN = 0
        result = ""
        p1 = 0
        p2 = 0
        bhuktilength = 0

        birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%Y')
        #print (birthdate)
        
        sub_days = birthdate + relativedelta(days=-tdec4)
        sub_months = sub_days + relativedelta(months=-tdec2)
        sub_years = sub_months + relativedelta(years=-tdec)
        
        startdate = sub_years
        #print ("Start Date : " + str(startdate))

  
        d = {}    
        
        for idasa in range(1, 10):
            #result = result + "\n***** idasa = " + str(idasa) + " ***** " + pname[idasa] + "\n"

            if idasa == 1:
                #d["maindasa{0}".format(idasa)] = StandardItem(pname[idasa].ljust(5) + " " + str(birthdate.strftime('%d-%m-%Y')) + " " + str(consumedperiod),10,color=QColor(0, 0, 0),language=language)
                d["maindasa{0}".format(idasa)] = StandardItem(pname[idasa].ljust(5) + " " + str(birthdate.strftime('%d-%m-%Y')),language=language)
            else:
                d["maindasa{0}".format(idasa)] = StandardItem(pname[idasa].ljust(5) + " " + str(startdate.strftime('%d-%m-%Y')) + " " + str(enddate.strftime('%d-%m-%Y')),12,color=QColor(0, 0, 0),language=language)
            
            b = {}
            for ibhukti in range(9):
                ibhuktiLord = idasa + ibhukti
                if ibhuktiLord > 9:
                    ibhuktiLord = ibhuktiLord - 9
     
                enddate = hora.Get_Bhukthi_Year_Month_Days(startdate, int(v_dasa[idasa]),int(v_dasa[ibhuktiLord]))

                b["bukthidasa{0}".format(ibhukti)] = StandardItem(pname[ibhuktiLord].ljust(5) + " " + str(startdate.strftime('%d-%m-%Y')) + " - " + str(enddate.strftime('%d-%m-%Y')),12,color=QColor(0, 0, 0),language=language)
                              
                d["maindasa{0}".format(idasa)].appendRow(b["bukthidasa{0}".format(ibhukti)])

                
                antharamstartdate = startdate

                s = {}
                for ianthra in range(9):
                    ianthraLord = ibhuktiLord + ianthra
                    if ianthraLord > 9:
                        ianthraLord = ianthraLord - 9
                
                    anthramperiod = hora.Get_Anthram_Year_Month_Days(antharamstartdate,int(v_dasa[idasa]),int(v_dasa[ibhuktiLord]), int(v_dasa[ianthraLord]))    

                    if ianthra == 8:
                        antharamenddate = enddate
                    else:
                        antharamenddate = anthramperiod

                        
                    s["sutchamadasa{0}".format(ianthra)] = StandardItem(pname[ianthraLord].ljust(5) + " " + str(antharamstartdate.strftime('%d-%m-%Y')) + " - " + str(antharamenddate.strftime('%d-%m-%Y')),12,color=QColor(0, 0, 0),language=language)
                    
                    b["bukthidasa{0}".format(ibhukti)].appendRow(s["sutchamadasa{0}".format(ianthra)])
                    
                    antharamstartdate = antharamenddate
  
                #result = result + "\n"
                #print (startdate)
                startdate = enddate
                
            rootNode.appendRow(d["maindasa{0}".format(idasa)])
                

        
        self.label_vim_dasa.setFont(fnt);
        
        self.label_vim_dasa.setText(consumedperiod_dasa)
        
        self.treeView_dasa.setModel(treeModel)
        #self.treeView_dasa.expandAll()

        return (str(consumedperiod_dasa))

    
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.

    mw = MainWindow()
    sys.exit(app.exec())
