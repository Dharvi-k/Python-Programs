import qrcode
import PIL

#Taking UPI ID as a input
upi_id=input("Enter your UPI ID: ")
amount=input("Enter the amount need to be received: ")
payee_name=input("Enter the payee name:")
t_note=input("Enter the Transaction note: ")

#(format):upi://pay?pa=UPI_ID&pr=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

#validate the inputs
if upi_id is None or not amount.isdigit():
    print("Invalid input. Please ensure the UPI ID is non-empty and the amount is a positive number.")

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment app you want to support

phonepe_url=f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&mc=1234&tn={t_note}"
paytm_url=f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&mc=1234&tn={t_note}"
google_pay_url=f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&mc=1234&tn={t_note}"

#create QR codes for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#Saving these QR codes to image files
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#Display these QR codes using PIL/Pillow library
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()


