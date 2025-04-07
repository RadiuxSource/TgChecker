/**
 * Telegram Translation Bot for bots.business
 * 
 * This is a complete, ready-to-use implementation that can be directly deployed to bots.business
 * It provides translation functionality with support for multiple languages
 * 
 * To use this in bots.business:
 * 1. Create a new bot on bots.business
 * 2. Copy the code sections below into the appropriate command handlers
 */

//---------------------------------------------------------------------
// MAIN LIBRARY - Copy this to "libs/translations.js" in bots.business
//---------------------------------------------------------------------

/**
 * Translation dictionary with common words and phrases
 */
const translations = {
  "es": {
    // Spanish translations
    "hello": "hola",
    "world": "mundo",
    "good morning": "buenos días",
    "good afternoon": "buenas tardes",
    "good evening": "buenas noches",
    "thank you": "gracias",
    "please": "por favor",
    "yes": "sí",
    "no": "no",
    "how are you": "cómo estás",
    "what is your name": "cómo te llamas",
    "my name is": "me llamo",
    "goodbye": "adiós",
    "help": "ayuda",
    "translate": "traducir",
    "news": "noticias"
  },
  "fr": {
    // French translations
    "hello": "bonjour",
    "world": "monde",
    "good morning": "bonjour",
    "good afternoon": "bon après-midi",
    "good evening": "bonsoir",
    "thank you": "merci",
    "please": "s'il vous plaît",
    "yes": "oui",
    "no": "non",
    "how are you": "comment allez-vous",
    "what is your name": "comment vous appelez-vous",
    "my name is": "je m'appelle",
    "goodbye": "au revoir",
    "help": "aide",
    "translate": "traduire",
    "news": "nouvelles"
  },
  "de": {
    // German translations
    "hello": "hallo",
    "world": "welt",
    "good morning": "guten morgen",
    "good afternoon": "guten tag",
    "good evening": "guten abend",
    "thank you": "danke",
    "please": "bitte",
    "yes": "ja",
    "no": "nein",
    "how are you": "wie geht es dir",
    "what is your name": "wie heißt du",
    "my name is": "ich heiße",
    "goodbye": "auf wiedersehen",
    "help": "hilfe",
    "translate": "übersetzen",
    "news": "nachrichten"
  },
  "it": {
    // Italian translations
    "hello": "ciao",
    "world": "mondo",
    "good morning": "buongiorno",
    "good afternoon": "buon pomeriggio",
    "good evening": "buonasera",
    "thank you": "grazie",
    "please": "per favore",
    "yes": "sì",
    "no": "no",
    "how are you": "come stai",
    "what is your name": "come ti chiami",
    "my name is": "mi chiamo",
    "goodbye": "arrivederci",
    "help": "aiuto",
    "translate": "tradurre",
    "news": "notizie"
  },
  "ru": {
    // Russian translations
    "hello": "привет",
    "world": "мир",
    "good morning": "доброе утро",
    "good afternoon": "добрый день",
    "good evening": "добрый вечер",
    "thank you": "спасибо",
    "please": "пожалуйста",
    "yes": "да",
    "no": "нет",
    "how are you": "как дела",
    "what is your name": "как вас зовут",
    "my name is": "меня зовут",
    "goodbye": "до свидания",
    "help": "помощь",
    "translate": "переводить",
    "news": "новости"
  },
  "zh": {
    // Chinese (Simplified) translations
    "hello": "你好",
    "world": "世界",
    "good morning": "早上好",
    "good afternoon": "下午好",
    "good evening": "晚上好",
    "thank you": "谢谢",
    "please": "请",
    "yes": "是",
    "no": "不",
    "how are you": "你好吗",
    "what is your name": "你叫什么名字",
    "my name is": "我的名字是",
    "goodbye": "再见",
    "help": "帮助",
    "translate": "翻译",
    "news": "新闻"
  }
};

/**
 * Language names for better user experience
 */
const languageNames = {
  "es": "Spanish",
  "fr": "French",
  "de": "German",
  "it": "Italian",
  "ru": "Russian",
  "zh": "Chinese"
};

/**
 * Clean and normalize language code input
 * 
 * @param {string} languageInput - Raw language input from user
 * @returns {string} - Cleaned language code or original if not recognized
 */
function cleanLanguageCode(languageInput) {
  const input = languageInput.toLowerCase().trim().replace(/["']/g, '');
  
  // Handle full language names
  const languageMap = {
    "spanish": "es",
    "español": "es",
    "french": "fr",
    "français": "fr",
    "german": "de",
    "deutsch": "de",
    "italian": "it",
    "italiano": "it",
    "russian": "ru",
    "русский": "ru",
    "chinese": "zh",
    "中文": "zh",
  };
  
  if (languageMap[input]) {
    return languageMap[input];
  }
  
  // Try to match short codes
  if (input.length <= 2) {
    return input;
  }
  
  // Extract language code if it appears in the input
  const codeMatch = input.match(/\b(es|fr|de|it|ru|zh)\b/);
  if (codeMatch) {
    return codeMatch[1];
  }
  
  // Default to the first two characters if nothing else matches
  return input.substring(0, 2);
}

/**
 * Translate text to the target language
 * 
 * @param {string} text - Text to translate 
 * @param {string} targetLang - Target language code
 * @returns {string} - Translated text
 */
function translateText(text, targetLang) {
  // Normalize language code
  const langCode = cleanLanguageCode(targetLang);
  
  // Check if language is supported
  if (!translations[langCode]) {
    return `${text} (Translation to ${langCode} not available)`;
  }
  
  // Get the dictionary for this language
  const langDict = translations[langCode];
  
  // Split the text into words and translate each one
  const words = text.toLowerCase().split(/\s+/);
  const translatedWords = words.map(word => {
    // Check for direct word translations
    if (langDict[word]) {
      return langDict[word];
    }
    
    // No translation found, return original word
    return word;
  });
  
  // Join the translated words back together
  let translatedText = translatedWords.join(" ");
  
  // Check for phrases (this is a simplified approach)
  Object.keys(langDict).forEach(phrase => {
    if (phrase.includes(" ") && text.toLowerCase().includes(phrase)) {
      translatedText = translatedText.replace(phrase, langDict[phrase]);
    }
  });
  
  // If no translation happened
  if (translatedText === text) {
    translatedText = `${text} (No translation available for these words)`;
  }
  
  return translatedText;
}

/**
 * Format the translation response for Telegram
 * 
 * @param {string} originalText - Original text
 * @param {string} translatedText - Translated text
 * @param {string} targetLang - Target language code
 * @returns {string} - Formatted message
 */
function formatTranslationResponse(originalText, translatedText, targetLang) {
  const langCode = cleanLanguageCode(targetLang);
  const targetLanguageName = languageNames[langCode] || langCode.toUpperCase();
  
  return `📝 Translation results:\n\n🔤 Original (English):\n${originalText}\n\n🔤 ${targetLanguageName}:\n${translatedText}`;
}

// Export the functions for use in commands
module.exports = {
  translateText,
  cleanLanguageCode,
  formatTranslationResponse,
  translations,
  languageNames
};

//---------------------------------------------------------------------
// START COMMAND - Copy this to the "/start" command in bots.business
//---------------------------------------------------------------------

function onStart() {
  return "👋 Welcome to TranslationBot! I can help you translate text between languages.\n\nType /help to see what I can do.";
}

// bots.business code:
function onCommand() {
  return onStart();
}


//---------------------------------------------------------------------
// HELP COMMAND - Copy this to the "/help" command in bots.business
//---------------------------------------------------------------------

function onHelp() {
  return "I can translate text from English to various languages.\n\nCommands:\n/start - Start the bot\n/help - Show this help message\n/translate - Translate text (follow format: /translate hello world)\n\nSupported languages:\n• Spanish (es)\n• French (fr)\n• German (de)\n• Italian (it)\n• Russian (ru)\n• Chinese (zh)";
}

// bots.business code:
function onCommand() {
  return onHelp();
}


//---------------------------------------------------------------------
// TRANSLATE COMMAND - Copy this to the "/translate" command in bots.business
//---------------------------------------------------------------------

function onTranslate() {
  // Check if there are parameters
  if (!params) {
    return "Please provide text to translate after the command, e.g., /translate hello world";
  }
  
  // Store the text to translate in user properties
  User.setProperty("textToTranslate", params, "string");
  User.setProperty("expectingLanguage", true, "boolean");
  
  // Ask for the target language
  return "Please specify the target language (e.g., \"es\" for Spanish, \"fr\" for French, \"de\" for German, \"it\" for Italian, \"ru\" for Russian, \"zh\" for Chinese)";
}

// bots.business code:
function onCommand() {
  return onTranslate();
}


//---------------------------------------------------------------------
// LANGUAGE RESPONSE HANDLER - Create a command with pattern "*" in bots.business
//---------------------------------------------------------------------

// Load the translation library
let Lib = require("Lib/translations.js");

function onMessage() {
  // Only process if we're expecting a language
  if (!User.getProperty("expectingLanguage")) {
    return;
  }
  
  // Get the text to translate
  const textToTranslate = User.getProperty("textToTranslate");
  if (!textToTranslate) {
    // Reset the property
    User.setProperty("expectingLanguage", false, "boolean");
    return "Sorry, I don't have any text to translate. Please use /translate with some text.";
  }
  
  // Reset the properties
  User.setProperty("textToTranslate", null, "string");
  User.setProperty("expectingLanguage", false, "boolean");
  
  // Clean the language code
  const langCode = Lib.cleanLanguageCode(message);
  
  // Check if the language is supported
  if (!Lib.translations[langCode]) {
    return `Sorry, the language "${message}" is not supported. Please use one of: es (Spanish), fr (French), de (German), it (Italian), ru (Russian), zh (Chinese)`;
  }
  
  // Translate the text
  const translatedText = Lib.translateText(textToTranslate, langCode);
  
  // Format and return the response
  return Lib.formatTranslationResponse(textToTranslate, translatedText, langCode);
}

// bots.business code:
function onCommand() {
  return onMessage();
}
