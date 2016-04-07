from reportlab.pdfgen import canvas
import reportlab
import PIL


def convert(tiff, out = "out.pdf"):
    outPDF = canvas.Canvas(out, pageCompression=1)
    img = PIL.Image.open(tiff)
    for page in range(img.n_frames):
        img.seek(page)
        imgPage = reportlab.lib.utils.ImageReader(img)
        outPDF.drawImage(imgPage, 0, 0, 595, 841)
        if page < img.n_frames:
            outPDF.showPage()
    outPDF.save()
    img.close()


if __name__ == "__main__":
    convert("scan.tif", "scan.pdf")