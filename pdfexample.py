import pandas as pd
import numpy as np
import pdfquery
import argparse


def write_to_excel(df):
	writer = pd.ExcelWriter('example_patient_data.xlsx')
	df.to_excel(writer,'Main',index=False)
	writer.save()

def clean_text_data(text):
	return text.split(':')[1]

def pdf_to_df(pdf_list):
	

	patient_data = {"Patient Number": [],
	               "Patient Name": [],
	               "DOB": [],
	               "Height": [],
	               "Weight": [],
	               "Diagnosis": [],
	               "Treatment": [],
	               "Recommendation": []}

	for i in pdf_list:
		pdf = pdfquery.PDFQuery(i)
		pdf.load()

		patient_data["Patient Number"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Patient Number")')\
				                                         .text()))
		patient_data["Patient Name"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Patient Name")')\
				                                         .text()))
		patient_data["DOB"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("DOB")')\
				                                         .text()))
		patient_data["Height"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Height")')\
				                                         .text()))
		patient_data["Weight"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Weight")')\
				                                         .text()))
		patient_data["Diagnosis"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Diagnosis")')\
				                                         .text()))
		patient_data["Treatment"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Treatment")')\
				                                         .text()))
		patient_data["Recommendation"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Recommendation")')\
				                                         .text()))
		
	columns=["Patient Number","Patient Name","DOB",
	"Height","Weight", "Diagnosis","Treatment","Recommendation"]
	pdata = pd.DataFrame.from_dict(patient_data)
	pdata = pdata[columns]

	return pdata

def main():

	#to_parse = ['samplepdf1.pdf','samplepdf2.pdf','samplepdf3.pdf','samplepdf4.pdf']

	parser = argparse.ArgumentParser(description = 'Parsing PDF tutorial')
	parser.add_argument('--parse', nargs='+', required=True)

	args = parser.parse_args()

	if args.parse:
		to_parse = args.parse


	pdata = pdf_to_df(to_parse)

	write_to_excel(pdata)

if __name__ == '__main__':
	main()
