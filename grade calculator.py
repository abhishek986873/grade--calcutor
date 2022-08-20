print('* INSTRUCTIONS')
print('-----------------------------------------------------------------------------')
print('* EACH SUBJECT IS OF 25 MARKS')
print('-----------------------------------------------------------------------------')
m1_maths=int(input('• ENTER YOUR MATHS MARKS: '))
m2_physics=int(input('• ENTER YOUR PHYSICS MARKS: '))
m3_chemistry=int(input('• ENTER YOUR CHEMISTRY MARKS: '))
m4_ip=int(input('• ENTER YOUR IP MARKS: '))

m_total=(m1_maths+m2_physics+m3_chemistry+m4_ip)
print('-----------------------------------------------------------------------------')
if (m_total>=90 and m_total<=100):
    print('• YOU GOT EXCELLENT GRADE')
if (m_total>=80 and m_total<=89):
    print("• YOU GOT 'A' GRADE")
if (m_total>=70 and m_total<=79):
    print("• YOU GOT 'B' GRADE")
if (m_total>=60 and m_total<=69):
    print("• YOU GOT 'C' GRADE ")
if (m_total>=50 and m_total<=59):
    print("• YOU GOT 'D' GRADE ")
