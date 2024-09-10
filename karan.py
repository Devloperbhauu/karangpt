import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TELEGRAM_TOKEN = '7520073325:AAGV2mRi_mdCgLAFcMikFMk-Xa10KkQ78Eg'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Pentest Bot! Use /help to see available commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "/scan - Get information on scanning tools\n"
        "/exploit - Learn about exploitation techniques\n"
        "/recon - Information on reconnaissance methods\n"
        "/report - Guidance on reporting findings\n"
    )
    update.message.reply_text(help_text)

def scan(update: Update, context: CallbackContext) -> None:
    scan_info = (
        "Scanning tools include:\n"
        "- Nmap: Network mapping and port scanning.\n"
        "- Nessus: Vulnerability scanning.\n"
        "- OpenVAS: Open-source vulnerability scanner.\n"
        "For detailed usage, refer to their official documentation."
    )
    update.message.reply_text(scan_info)

def exploit(update: Update, context: CallbackContext) -> None:
    exploit_info = (
        "Common exploitation techniques:\n"
        "- SQL Injection: Exploiting input fields.\n"
        "- Cross-Site Scripting (XSS): Injecting scripts into web pages.\n"
        "- Buffer Overflow: Overwriting memory to execute arbitrary code.\n"
        "Always ensure you have permission before testing."
    )
    update.message.reply_text(exploit_info)

def recon(update: Update, context: CallbackContext) -> None:
    recon_info = (
        "Reconnaissance methods include:\n"
        "- WHOIS Lookup: Gather domain registration information.\n"
        "- DNS Enumeration: Discover subdomains and IP addresses.\n"
        "- Social Engineering: Gather information through human interaction.\n"
    )
    update.message.reply_text(recon_info)

def report(update: Update, context: CallbackContext) -> None:
    report_info = (
        "When reporting findings:\n"
        "- Include an executive summary.\n"
        "- Detail vulnerabilities and their impact.\n"
        "- Provide remediation steps.\n"
    )
    update.message.reply_text(report_info)

def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("scan", scan))
    dispatcher.add_handler(CommandHandler("exploit", exploit))
    dispatcher.add_handler(CommandHandler("recon", recon))
    dispatcher.add_handler(CommandHandler("report", report))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()