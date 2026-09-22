// Numbers match days/01-line-that-misses/fit_line.py
const DAYS = [1, 2, 3, 4, 5];
const CLOSES = [2.1, 3.9, 6.2, 20, 10.4];
const LINE_AT = [1.98, 5.25, 8.52, 11.79, 15.06];
const ASK = 3;

const canvas = document.querySelector("#sky");
const ctx = canvas.getContext("2d");
const readout = document.querySelector("#readout");
const oath = document.querySelector("#oath");

const pad = { l: 56, r: 24, t: 28, b: 42 };

function xAt(i) {
  const inner = canvas.width - pad.l - pad.r;
  return pad.l + (inner * i) / (DAYS.length - 1);
}

function yAt(price) {
  const inner = canvas.height - pad.t - pad.b;
  const min = 0;
  const max = 22;
  return pad.t + inner * (1 - (price - min) / (max - min));
}

function frame(t) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = "#1c3344";
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(pad.l, pad.t);
  ctx.lineTo(pad.l, canvas.height - pad.b);
  ctx.lineTo(canvas.width - pad.r, canvas.height - pad.b);
  ctx.stroke();

  ctx.fillStyle = "#7f93a1";
  ctx.font = "13px sans-serif";
  DAYS.forEach((day, i) => {
    ctx.fillText(`第${day}日`, xAt(i) - 16, canvas.height - 16);
  });

  const shown = Math.min(DAYS.length, Math.floor(t / 18));
  for (let i = 0; i < shown; i += 1) {
    const spike = i === ASK;
    ctx.fillStyle = spike ? "#f0b45a" : "#d7e2ea";
    ctx.beginPath();
    ctx.arc(xAt(i), yAt(CLOSES[i]), spike ? 6 : 4, 0, Math.PI * 2);
    ctx.fill();
  }

  if (shown > ASK && t > 90) {
    ctx.fillStyle = "#f0b45a";
    ctx.fillText("异常拉高 20", xAt(ASK) - 28, yAt(20) - 14);
  }

  const lineT = Math.max(0, Math.min(1, (t - 110) / 50));
  if (lineT > 0) {
    ctx.strokeStyle = "#7ec8ff";
    ctx.lineWidth = 2;
    ctx.beginPath();
    const end = lineT * (DAYS.length - 1);
    const whole = Math.floor(end);
    ctx.moveTo(xAt(0), yAt(LINE_AT[0]));
    for (let i = 1; i <= whole; i += 1) ctx.lineTo(xAt(i), yAt(LINE_AT[i]));
    if (whole < DAYS.length - 1) {
      const frac = end - whole;
      const x0 = xAt(whole);
      const y0 = yAt(LINE_AT[whole]);
      const x1 = xAt(whole + 1);
      const y1 = yAt(LINE_AT[whole + 1]);
      ctx.lineTo(x0 + (x1 - x0) * frac, y0 + (y1 - y0) * frac);
    }
    ctx.stroke();
  }

  const gapT = Math.max(0, Math.min(1, (t - 165) / 24));
  if (gapT > 0) {
    const x = xAt(ASK);
    const yTop = yAt(CLOSES[ASK]);
    const yBot = yAt(LINE_AT[ASK]);
    const y = yTop + (yBot - yTop) * gapT;
    ctx.strokeStyle = "#f0b45a";
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(x, yTop);
    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "#7ec8ff";
    ctx.fillText("直线 11.79", x + 14, yBot + 4);
    if (gapT > 0.85) {
      ctx.fillStyle = "#f0b45a";
      ctx.fillText("失手 8.2", x + 14, (yTop + yBot) / 2);
    }
  }

  readout.hidden = t < 190;
  oath.hidden = t < 205;
}

let tick = 0;
let timer = 0;

function play() {
  window.clearInterval(timer);
  tick = 0;
  readout.hidden = true;
  oath.hidden = true;
  timer = window.setInterval(() => {
    tick += 1;
    frame(tick);
    if (tick > 210) window.clearInterval(timer);
  }, 32);
}

document.querySelector("#replay").addEventListener("click", play);
window.renderFrame = frame;

const still = new URLSearchParams(location.search).get("t");
if (still == null) play();
else frame(Number(still));
