def otp_body(otp: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Your OTP Code</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background: #f4f4f4;
          padding: 20px;
          color: #333;
        }}
        .container {{
          max-width: 500px;
          margin: auto;
          background: #ffffff;
          padding: 30px;
          border-radius: 8px;
          box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .otp {{
          font-size: 24px;
          font-weight: bold;
          background: #f0f0f0;
          padding: 15px;
          text-align: center;
          border-radius: 5px;
          letter-spacing: 5px;
          margin: 20px 0;
          color: #007BFF;
        }}
        .footer {{
          font-size: 12px;
          color: #888;
          text-align: center;
          margin-top: 30px;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h2>Hello 👋,</h2>
        <p>Here is your One-Time Password (OTP) for verification:</p>
        <div class="otp">{otp}</div>
        <p>This code will expire in 5 minutes. Please do not share this code with anyone.</p>
        <p>Thanks,<br>The FastAPI Team</p>
        <div class="footer">
          © 2025 FastAPI App. All rights reserved.
        </div>
      </div>
    </body>
    </html>
    """