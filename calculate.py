#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, html, datetime
VERSION = "STYLE-2025-09-16"  # ← これが出ていれば新ファイル！

def fail(msg):
    print("Content-Type: text/html; charset=UTF-8\n")
    print(f"<h2>Error</h2><p>{html.escape(msg)}</p>")
    sys.exit(1)

# 期待: 引数 a b c（数値）
if len(sys.argv) != 4:
    fail("Usage: calculate.py <a> <b> <c>")

try:
    a = float(sys.argv[1]); b = float(sys.argv[2]); c = float(sys.argv[3])
except ValueError:
    fail("Inputs must be numeric")
if a == 0:
    fail("Division by zero (a must not be 0)")

# 手順: c^3 → √ → ÷a → ×10 → +b
c_cubed = c ** 3
sqrt_c3 = c_cubed ** 0.5
step3   = sqrt_c3 / a
step4   = step3 * 10
final_result = step4 + b

def fmt(x): return f"{x:.1f}"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
last_name = "Umebara"  # ここを自分の名字に変えてOK

print("Content-Type: text/html; charset=UTF-8\n")
print(f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><title>Assignment #2</title>
  <style>
    body {{ background:#f4e6d7; font-family:Arial,Helvetica,sans-serif; color:#333; padding:24px; }}
    .card {{ background:#fffaf3; border:1px solid #e2c9aa; padding:18px 22px; max-width:720px; box-shadow:0 1px 2px rgba(0,0,0,.05); }}
    h1,h2 {{ margin:6px 0; }} .title {{ color:#2b8a3e; font-weight:800; }}
    .block {{ background:#fff; border:1px solid #e2c9aa; padding:12px 16px; position:relative; margin-top:10px; white-space:pre-wrap; font-family:Menlo,Consolas,monospace; }}
    .block:before {{ content:""; position:absolute; left:0; top:0; bottom:0; width:6px; background:#2ecc71; }}
    .muted {{ color:#6b6b6b; font-style:italic; }}
    .hr {{ border-top:2px solid #c7ac8a; margin:12px 0 16px; }}
    .mono {{ font-family:Menlo,Consolas,monospace; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="mono" style="margin-bottom:10px;">
      Example of Output (http://&lt;Public_IP&gt;/calculate?a=2&b=3&c=4) • {VERSION}
    </div>
    <div class="hr"></div>

    <h2 class="title">Assignment #2</h2>
    <div>Your_{last_name}</div>

    <div class="hr"></div>

    <h2>Final Result: {fmt(final_result)}</h2>

    <div class="block">
Step 1: c = {fmt(c)},  c^3 = {fmt(c_cubed)}
Step 2: √(c^3) = {fmt(sqrt_c3)}
Step 3: {fmt(sqrt_c3)} / {fmt(a)} = {fmt(step3)}
Step 4: {fmt(step3)} × 10 = {fmt(step4)}
Step 5: {fmt(step4)} + {fmt(b)} = {fmt(final_result)}
    </div>

    <p class="muted">Calculation completed at {timestamp}</p>
    <div class="hr"></div>
  </div>
</body>
</html>
""")
