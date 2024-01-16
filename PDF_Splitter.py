import PyPDF2
import sys

# قراءة اسم الملف وعدد الصفحات من المعطيات
file_name = sys.argv[1]
pages_per_file = int(sys.argv[2])

# فتح ملف PDF المصدر
source_pdf = open(file_name, "rb")
pdf_reader = PyPDF2.PdfFileReader(source_pdf)

# الحصول على عدد الصفحات في الملف
total_pages = pdf_reader.getNumPages()

# حساب عدد الملفات المقسمة المطلوبة
num_files = (total_pages + pages_per_file - 1) // pages_per_file

# تكرار على كل ملف مقسم
for i in range(num_files):
    # إنشاء كائن PdfFileWriter لكتابة الملف المقسم
    pdf_writer = PyPDF2.PdfFileWriter()

    # تحديد نطاق الصفحات للملف المقسم
    start_page = i * pages_per_file
    end_page = min((i + 1) * pages_per_file, total_pages)

    # إضافة الصفحات من الملف المصدر إلى الملف المقسم
    for j in range(start_page, end_page):
        pdf_writer.addPage(pdf_reader.getPage(j))

    # فتح ملف PDF الهدف للكتابة
    target_pdf = open(f"file{i + 1}.pdf", "wb")

    # كتابة الملف المقسم إلى الملف الهدف
    pdf_writer.write(target_pdf)

    # إغلاق الملف الهدف
    target_pdf.close()

# إغلاق الملف المصدر
source_pdf.close()
