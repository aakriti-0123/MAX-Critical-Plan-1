<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Full Screen Sheet Embeds</title>
  <style>
    html, body {
      height: 100%;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #faf5f3;
    }
    .sheet-embed-container {
      width: 100vw;
      height: 100vh;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
    }
    .sheet-instructions {
      font-family: Arial, sans-serif;
      font-size: 1.15rem;
      margin: 18px 0 10px 0;
      text-align: center;
      background: transparent;
      color: #222;
      z-index: 2;
    }
    .tabs {
      display: flex;
      justify-content: center;
      background: #f0ecec;
      border-bottom: 1px solid #ddd;
    }
    .tab-btn {
      font-size: 1rem;
      font-family: Arial, sans-serif;
      padding: 12px 28px;
      background: none;
      border: none;
      border-bottom: 3px solid transparent;
      cursor: pointer;
      transition: border-bottom 0.2s, background 0.2s;
      color: #333;
      outline: none;
    }
    .tab-btn.active {
      border-bottom: 3px solid #0078d7;
      background: #fff;
      font-weight: bold;
    }
    .iframe-wrapper {
      flex: 1 1 auto;
      width: 100vw;
      height: 100%;
      position: relative;
      min-width: 0;
      min-height: 0;
    }
    .sheet-iframe {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      width: 100%;
      height: 100%;
      border: none;
      display: none;
      background: #fff;
    }
    .sheet-iframe.active {
      display: block;
    }
  </style>
</head>
<body>
  <div class="sheet-embed-container">
    <div class="sheet-instructions">
      Please navigate to the tab named <b>REGULAR CP_30D</b> in the embedded sheet below.
    </div>
    <div class="tabs">
      <button class="tab-btn active" data-iframe="wn26">wn26</button>
      <button class="tab-btn" data-iframe="ss26">ss26</button>
      <button class="tab-btn" data-iframe="wn25">wn25</button>
    </div>
    <div class="iframe-wrapper">
      <iframe
        class="sheet-iframe active"
        id="iframe-wn26"
        src="https://docs.google.com/spreadsheets/d/1DioMTxZakUrLg5ZjElWo9DcxVPxcqhUN/preview"
        allowfullscreen
        loading="lazy"
      ></iframe>
      <iframe
        class="sheet-iframe"
        id="iframe-ss26"
        src="https://docs.google.com/spreadsheets/d/16XNqVsbEYVxUBvRyF9l6EgkT_p5lDvQy/preview"
        allowfullscreen
        loading="lazy"
      ></iframe>
      <iframe
        class="sheet-iframe"
        id="iframe-wn25"
        src="https://docs.google.com/spreadsheets/d/1mXSf7Kx89WZb4Off7x3tPa3Buc6QF1Dj/preview"
        allowfullscreen
        loading="lazy"
      ></iframe>
    </div>
  </div>
  <script>
    // Tab switching logic
    const tabs = document.querySelectorAll('.tab-btn');
    const iframes = {
      wn26: document.getElementById('iframe-wn26'),
      ss26: document.getElementById('iframe-ss26'),
      wn25: document.getElementById('iframe-wn25')
    };

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        // Set active tab
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        // Show corresponding iframe
        Object.keys(iframes).forEach(key => {
          iframes[key].classList.remove('active');
        });
        iframes[tab.dataset.iframe].classList.add('active');
      });
    });
  </script>
</body>
</html>
