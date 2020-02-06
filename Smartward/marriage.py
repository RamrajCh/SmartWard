# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'marriage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import nepali_date
import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sw_string
import dbconnect


class Ui_MarriageForm(object):
    def setupUi(self, MarriageForm):
        MarriageForm.setObjectName("MarriageForm")
        MarriageForm.resize(811, 957)
        self.centralwidget = QtWidgets.QWidget(MarriageForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -324, 777, 1261))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.marriageTypeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.marriageTypeLabel.setObjectName("marriageTypeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.marriageTypeLabel)
        self.marriageTypeComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.marriageTypeComboBox.setObjectName("marriageTypeComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.marriageTypeComboBox)
        self.marriageDateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.marriageDateLabel.setObjectName("marriageDateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.marriageDateLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_2.setDisplayFormat("yyyy/MM/dd")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.locationOfMarriageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.locationOfMarriageLabel.setObjectName("locationOfMarriageLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.locationOfMarriageLabel)
        self.districtLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel.setObjectName("districtLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.districtLabel)
        self.districtLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit.setObjectName("districtLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.districtLineEdit)
        self.municipalityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.municipalityLabel.setObjectName("municipalityLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.municipalityLabel)
        self.municipalityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.municipalityLineEdit.setObjectName("municipalityLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.municipalityLineEdit)
        self.wardNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel.setObjectName("wardNoLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel)
        self.wardNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.wardNoLineEdit.setObjectName("wardNoLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit)
        self.roadLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.roadLabel.setObjectName("roadLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.roadLabel)
        self.roadStreetLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.roadStreetLineEdit.setObjectName("roadStreetLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.roadStreetLineEdit)
        self.villageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.villageLabel.setObjectName("villageLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.villageLabel)
        self.villageLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.villageLineEdit.setObjectName("villageLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.villageLineEdit)
        self.houseNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.houseNoLabel.setObjectName("houseNoLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.houseNoLabel)
        self.houseNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.houseNoLineEdit.setObjectName("houseNoLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.houseNoLineEdit)
        self.locationIfMarriageAbroadLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.locationIfMarriageAbroadLabel.setObjectName("locationIfMarriageAbroadLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.locationIfMarriageAbroadLabel)
        self.locationIfMarriageAbroadLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.locationIfMarriageAbroadLineEdit.setObjectName("locationIfMarriageAbroadLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.locationIfMarriageAbroadLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.nameLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLabel_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.lastnameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lastnameLabel.setObjectName("lastnameLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastnameLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.fullNameLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fullNameLabel_2.setObjectName("fullNameLabel_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.dateOfBirthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.dateOfBirthLabel)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_7.addWidget(self.lineEdit_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_7.addWidget(self.lineEdit_7)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.casteLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.casteLabel_2.setObjectName("casteLabel_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.casteLabel_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_8.addWidget(self.lineEdit_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_8.addWidget(self.lineEdit_9)
        self.formLayout_2.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.qualificationLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.qualificationLabel_2.setObjectName("qualificationLabel_2")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.qualificationLabel_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_9.addWidget(self.lineEdit_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_9.addWidget(self.lineEdit_11)
        self.formLayout_2.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.occupationLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.occupationLabel_2.setObjectName("occupationLabel_2")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.occupationLabel_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_10.addWidget(self.lineEdit_14)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_10.addWidget(self.lineEdit_13)
        self.formLayout_2.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.preMaritalStatusLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.preMaritalStatusLabel_2.setObjectName("preMaritalStatusLabel_2")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.preMaritalStatusLabel_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_11.addWidget(self.lineEdit_16)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_11.addWidget(self.lineEdit_15)
        self.formLayout_2.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.permanentAdressLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.permanentAdressLabel_2.setObjectName("permanentAdressLabel_2")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.permanentAdressLabel_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.formLayout_2.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.districtLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel_3.setObjectName("districtLabel_3")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.districtLabel_3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.horizontalLayout_13.addWidget(self.lineEdit_18)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_13.addWidget(self.lineEdit_17)
        self.formLayout_2.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.municipalityLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.municipalityLabel_3.setObjectName("municipalityLabel_3")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.municipalityLabel_3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.horizontalLayout_14.addWidget(self.lineEdit_20)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_14.addWidget(self.lineEdit_19)
        self.formLayout_2.setLayout(11, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.wardNoLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel_3.setObjectName("wardNoLabel_3")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_15.addWidget(self.lineEdit_21)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.horizontalLayout_15.addWidget(self.lineEdit_22)
        self.formLayout_2.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_15)
        self.roadStreetLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.roadStreetLabel.setObjectName("roadStreetLabel")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.roadStreetLabel)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.horizontalLayout_16.addWidget(self.lineEdit_24)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.horizontalLayout_16.addWidget(self.lineEdit_23)
        self.formLayout_2.setLayout(13, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_16)
        self.villageCommunityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.villageCommunityLabel.setObjectName("villageCommunityLabel")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.villageCommunityLabel)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.horizontalLayout_17.addWidget(self.lineEdit_26)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.horizontalLayout_17.addWidget(self.lineEdit_25)
        self.formLayout_2.setLayout(14, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_17)
        self.houseNoLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.houseNoLabel_3.setObjectName("houseNoLabel_3")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.houseNoLabel_3)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.horizontalLayout_21.addWidget(self.lineEdit_28)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.horizontalLayout_21.addWidget(self.lineEdit_27)
        self.formLayout_2.setLayout(15, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_21)
        self.birthCountryLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.birthCountryLabel_2.setObjectName("birthCountryLabel_2")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.birthCountryLabel_2)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.horizontalLayout_22.addWidget(self.lineEdit_30)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.horizontalLayout_22.addWidget(self.lineEdit_29)
        self.formLayout_2.setLayout(16, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_22)
        self.countryWithCitizenshipLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.countryWithCitizenshipLabel_2.setObjectName("countryWithCitizenshipLabel_2")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.countryWithCitizenshipLabel_2)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.horizontalLayout_23.addWidget(self.lineEdit_32)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.horizontalLayout_23.addWidget(self.lineEdit_31)
        self.formLayout_2.setLayout(17, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_23)
        self.citizenshipNoLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoLabel_2.setObjectName("citizenshipNoLabel_2")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoLabel_2)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.horizontalLayout_33.addWidget(self.lineEdit_34)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.horizontalLayout_33.addWidget(self.lineEdit_33)
        self.formLayout_2.setLayout(18, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_33)
        self.issueDateLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.issueDateLabel_2.setObjectName("issueDateLabel_2")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.issueDateLabel_2)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.horizontalLayout_32.addWidget(self.lineEdit_36)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.horizontalLayout_32.addWidget(self.lineEdit_35)
        self.formLayout_2.setLayout(19, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_32)
        self.issueDistrictLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.issueDistrictLabel_2.setObjectName("issueDistrictLabel_2")
        self.formLayout_2.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.issueDistrictLabel_2)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.horizontalLayout_34.addWidget(self.lineEdit_38)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.horizontalLayout_34.addWidget(self.lineEdit_37)
        self.formLayout_2.setLayout(20, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_34)
        self.passportNoIfForeignLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.passportNoIfForeignLabel_2.setObjectName("passportNoIfForeignLabel_2")
        self.formLayout_2.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.passportNoIfForeignLabel_2)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.horizontalLayout_25.addWidget(self.lineEdit_40)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.horizontalLayout_25.addWidget(self.lineEdit_39)
        self.formLayout_2.setLayout(21, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_25)
        self.countryIfForeignLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.countryIfForeignLabel_2.setObjectName("countryIfForeignLabel_2")
        self.formLayout_2.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.countryIfForeignLabel_2)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.horizontalLayout_35.addWidget(self.lineEdit_42)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.horizontalLayout_35.addWidget(self.lineEdit_41)
        self.formLayout_2.setLayout(22, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_35)
        self.adressIfForeignLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.adressIfForeignLabel_2.setObjectName("adressIfForeignLabel_2")
        self.formLayout_2.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.adressIfForeignLabel_2)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.horizontalLayout_36.addWidget(self.lineEdit_44)
        self.lineEdit_43 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.horizontalLayout_36.addWidget(self.lineEdit_43)
        self.formLayout_2.setLayout(23, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_36)
        self.grandfatherNameLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.grandfatherNameLabel_2.setObjectName("grandfatherNameLabel_2")
        self.formLayout_2.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.grandfatherNameLabel_2)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.horizontalLayout_37.addWidget(self.lineEdit_46)
        self.lineEdit_45 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.horizontalLayout_37.addWidget(self.lineEdit_45)
        self.formLayout_2.setLayout(24, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_37)
        self.fatherNameLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fatherNameLabel_2.setObjectName("fatherNameLabel_2")
        self.formLayout_2.setWidget(25, QtWidgets.QFormLayout.LabelRole, self.fatherNameLabel_2)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.horizontalLayout_38.addWidget(self.lineEdit_48)
        self.lineEdit_47 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.horizontalLayout_38.addWidget(self.lineEdit_47)
        self.formLayout_2.setLayout(25, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_38)
        self.motherNameLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.motherNameLabel_2.setObjectName("motherNameLabel_2")
        self.formLayout_2.setWidget(26, QtWidgets.QFormLayout.LabelRole, self.motherNameLabel_2)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.horizontalLayout_39.addWidget(self.lineEdit_50)
        self.lineEdit_49 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.horizontalLayout_39.addWidget(self.lineEdit_49)
        self.formLayout_2.setLayout(26, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_39)
        self.jhLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.jhLabel.setText("")
        self.jhLabel.setObjectName("jhLabel")
        self.formLayout_2.setWidget(27, QtWidgets.QFormLayout.LabelRole, self.jhLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(27, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.gridLayout_2.addLayout(self.formLayout_2, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        MarriageForm.setCentralWidget(self.centralwidget)

        self.marriageTypeComboBox.addItems(['Social Tradition','Marriage Registration Act 2028'])

        self.retranslateUi(MarriageForm)
        QtCore.QMetaObject.connectSlotsByName(MarriageForm)

    def retranslateUi(self, MarriageForm):
        _translate = QtCore.QCoreApplication.translate
        MarriageForm.setWindowTitle(_translate("MarriageForm", "Marriage Form"))
        self.label.setText(_translate("MarriageForm", "<b>Details Of Marriage</b>"))
        self.marriageTypeLabel.setText(_translate("MarriageForm", "Marriage Type"))
        self.marriageDateLabel.setText(_translate("MarriageForm", "Marriage Date"))
        self.locationOfMarriageLabel.setText(_translate("MarriageForm", "<b>Location Of marriage</b>"))
        self.districtLabel.setText(_translate("MarriageForm", "District"))
        self.municipalityLabel.setText(_translate("MarriageForm", "Municipality"))
        self.wardNoLabel.setText(_translate("MarriageForm", "Ward No"))
        self.roadLabel.setText(_translate("MarriageForm", "Road/street"))
        self.villageLabel.setText(_translate("MarriageForm", "village"))
        self.houseNoLabel.setText(_translate("MarriageForm", "House No"))
        self.locationIfMarriageAbroadLabel.setText(_translate("MarriageForm", "Location if Marriage Abroad"))
        self.label_5.setText(_translate("MarriageForm", "Bride"))
        self.label_2.setText(_translate("MarriageForm", "Bridegroom"))
        self.nameLabel_2.setText(_translate("MarriageForm", "<b>Name</b>"))
        self.lastnameLabel.setText(_translate("MarriageForm", "Lastname"))
        self.fullNameLabel_2.setText(_translate("MarriageForm", "Full name"))
        self.dateOfBirthLabel.setText(_translate("MarriageForm", "Date of Birth"))
        self.casteLabel_2.setText(_translate("MarriageForm", "Caste"))
        self.qualificationLabel_2.setText(_translate("MarriageForm", "Qualification"))
        self.occupationLabel_2.setText(_translate("MarriageForm", "Occupation"))
        self.preMaritalStatusLabel_2.setText(_translate("MarriageForm", "Pre-marital status"))
        self.permanentAdressLabel_2.setText(_translate("MarriageForm", "<b>Permanent Address</b>"))
        self.districtLabel_3.setText(_translate("MarriageForm", "District"))
        self.municipalityLabel_3.setText(_translate("MarriageForm", "Municipality"))
        self.wardNoLabel_3.setText(_translate("MarriageForm", "Ward No"))
        self.roadStreetLabel.setText(_translate("MarriageForm", "Road/street"))
        self.villageCommunityLabel.setText(_translate("MarriageForm", "Village/community"))
        self.houseNoLabel_3.setText(_translate("MarriageForm", "House No"))
        self.birthCountryLabel_2.setText(_translate("MarriageForm", "Birth Country"))
        self.countryWithCitizenshipLabel_2.setText(_translate("MarriageForm", "Country With citizenship"))
        self.citizenshipNoLabel_2.setText(_translate("MarriageForm", "Citizenship No"))
        self.issueDateLabel_2.setText(_translate("MarriageForm", "Issue Date"))
        self.issueDistrictLabel_2.setText(_translate("MarriageForm", "Issue District"))
        self.passportNoIfForeignLabel_2.setText(_translate("MarriageForm", "Passport No(if foreign)"))
        self.countryIfForeignLabel_2.setText(_translate("MarriageForm", "country(if foreign)"))
        self.adressIfForeignLabel_2.setText(_translate("MarriageForm", "Adress(if foreign)"))
        self.grandfatherNameLabel_2.setText(_translate("MarriageForm", "Grandfather Name"))
        self.fatherNameLabel_2.setText(_translate("MarriageForm", "Father Name"))
        self.motherNameLabel_2.setText(_translate("MarriageForm", "Mother Name"))
        self.label_6.setText(_translate("MarriageForm", "<b>Details Of Spouse</b>"))

class ActualWork():
    def __init__(self):
        self.MarriageForm = QtWidgets.QMainWindow()
        self.ui = Ui_MarriageForm()
        self.ui.setupUi(self.MarriageForm)
        self.MarriageForm.show()
        self.actualWork()

    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda:self.MarriageForm.close())

    def submitform(self):
        self.values=self.getallvalues()
        a = sw_string.generateList(**self.values)
        #['detailsofmarriage', ('Social Tradition', ('2000-01-01', '2056/09/17')), 'locationofmarriage', ('Kavre', 'Namobudda', '04', 'Timal Road', 'Methinkot', '45', ''), 'detailsofspouse', {'detailsofbride': ('Tandon', 'Rabina', '2057/01/05', 'Kami', '+2', 'Actress', 'Divorcee', ('Rampur', 'Narayanghat', '5', 'Ghandi Street', 'Hariharpur', '78', 'India'), ('India', '27-12398721', '2071/06/09', 'Rampur', '87289398', 'India', 'New Delhi'), ('Fariha Tandon', 'Kanod Tandon', 'Kajol Tandon')), 'detailsofbridegroom': ('Ghimere', 'Tilak', '2051/03/21', 'Brahmin', 'B.Sc.', 'Astrologer', 'Single', ('Solukhumbu', 'Namche Bazar', '9', 'Manila Street', 'Vaisepati', '567', 'Nepal'), ('Nepal', '983-3468', '2067/03/05', 'Solukhumbu', '', '', ''), ('Goshnath Ghimere', 'Farilal Ghimere', 'Nabina Ghimere'))}]


    def getallvalues(self):
        self.marriagetype=self.ui.marriageTypeComboBox.currentText()
        date=QDate(self.ui.dateEdit_2.date())
        year,month,day=date.getDate()
        marriage_in_ad=datetime.date(year,month,day)
        marriage_in_bs=nepali_date.NepaliDate.to_nepali_date(marriage_in_ad)
        print(str(marriage_in_bs))
        self.marriagedate=(str(marriage_in_ad),str(marriage_in_bs)[3:])
        detailsofmarriage=(self.marriagetype,self.marriagedate)
        locationofmarriage=(self.ui.districtLineEdit.text(),self.ui.municipalityLineEdit.text(),self.ui.wardNoLineEdit.text(),self.ui.roadStreetLineEdit.text(),self.ui.villageLineEdit.text(),self.ui.houseNoLineEdit.text(),self.ui.locationIfMarriageAbroadLineEdit.text())

        self.paddressbride=(self.ui.lineEdit_18.text(),self.ui.lineEdit_20.text(),self.ui.lineEdit_21.text(),self.ui.lineEdit_24.text(),self.ui.lineEdit_26.text(),self.ui.lineEdit_28.text(),self.ui.lineEdit_30.text())
        self.ccbride=(self.ui.lineEdit_32.text(),self.ui.lineEdit_34.text(),self.ui.lineEdit_36.text(),self.ui.lineEdit_38.text(),self.ui.lineEdit_40.text(),self.ui.lineEdit_42.text(),self.ui.lineEdit_44.text())
        self.parentbride=(self.ui.lineEdit_46.text(),self.ui.lineEdit_48.text(),self.ui.lineEdit_50.text())
        self.detailsofbride=(self.ui.lineEdit_4.text(),self.ui.lineEdit_6.text(),self.ui.lineEdit_8.text(),self.ui.lineEdit_10.text(),self.ui.lineEdit_12.text(),self.ui.lineEdit_14.text(),self.ui.lineEdit_16.text(),self.paddressbride,self.ccbride,self.parentbride)

        self.paddressbridegroom=(self.ui.lineEdit_17.text(),self.ui.lineEdit_19.text(),self.ui.lineEdit_22.text(),self.ui.lineEdit_23.text(),self.ui.lineEdit_25.text(),self.ui.lineEdit_27.text(),self.ui.lineEdit_29.text())
        self.ccbridegroom=(self.ui.lineEdit_31.text(),self.ui.lineEdit_33.text(),self.ui.lineEdit_35.text(),self.ui.lineEdit_37.text(),self.ui.lineEdit_39.text(),self.ui.lineEdit_41.text(),self.ui.lineEdit_43.text())
        self.parentbridegroom=(self.ui.lineEdit_45.text(),self.ui.lineEdit_47.text(),self.ui.lineEdit_49.text())
        self.detailsofbridegroom=(self.ui.lineEdit_3.text(),self.ui.lineEdit_5.text(),self.ui.lineEdit_7.text(),self.ui.lineEdit_9.text(),self.ui.lineEdit_11.text(),self.ui.lineEdit_13.text(),self.ui.lineEdit_15.text(),self.paddressbridegroom,self.ccbridegroom,self.parentbridegroom)
        detailsofspouse={'detailsofbride':self.detailsofbride, 'detailsofbridegroom':self.detailsofbridegroom}

        return {"detailsofmarriage":detailsofmarriage , "locationofmarriage":locationofmarriage , 'detailsofspouse':detailsofspouse}

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    """
    MainWindow = QtWidgets.QMainWindow()
    ui = ActualWork()
    ui.setupUi(MainWindow)
    MainWindow.show()
    """
    sys.exit(app.exec_())