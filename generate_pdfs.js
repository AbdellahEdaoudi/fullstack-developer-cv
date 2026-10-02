const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
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
    await page.goto(`file:///${filePath.replace(/\\/g, '/')}`, { waitUntil: 'networkidle0' });
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
  console.log('All PDFs generated successfully!');
})();



