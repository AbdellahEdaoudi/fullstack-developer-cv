import subprocess
import os

# Generate PDFs using node / Puppeteer
node_pdf_script = '''
const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe',
    headless: 'new'
  });
  
  const files = [
    { html: 'cv_en.html', pdf: 'cv-abdellah-edaoudi-en.pdf' },
    { html: 'cv_fr.html', pdf: 'cv-abdellah-edaoudi-fr.pdf' },
    { html: 'cv_es.html', pdf: 'cv-abdellah-edaoudi-es.pdf' },
    { html: 'cv_de.html', pdf: 'cv-abdellah-edaoudi-de.pdf' },
    { html: 'cv_nl.html', pdf: 'cv-abdellah-edaoudi-nl.pdf' },
    { html: 'cv_it.html', pdf: 'cv-abdellah-edaoudi-it.pdf' },
    { html: 'cv_pt.html', pdf: 'cv-abdellah-edaoudi-pt.pdf' },
    { html: 'cv_ar.html', pdf: 'cv-abdellah-edaoudi-ar.pdf' }
  ];

  for (const item of files) {
    const page = await browser.newPage();
    const filePath = path.join(__dirname, item.html);
    await page.goto(`file:///${filePath.replace(/\\\\/g, '/')}`, { waitUntil: 'networkidle0' });
    await page.pdf({
      path: path.join(__dirname, item.pdf),
      format: 'A4',
      printBackground: true,
      margin: { top: '0px', right: '0px', bottom: '0px', left: '0px' }
    });
    await page.close();
    console.log(`Generated ${item.pdf}`);
  }

  await browser.close();
})();
'''

with open('temp_gen_pdfs.js', 'w', encoding='utf-8') as f:
    f.write(node_pdf_script)

subprocess.run(['node', 'temp_gen_pdfs.js'], check=True)

if os.path.exists('temp_gen_pdfs.js'):
    os.remove('temp_gen_pdfs.js')

print('All PDFs generated successfully!')



