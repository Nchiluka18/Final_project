

# 🍎 Neural Nexus – AI-Powered Fruit Benefits Companion on Discord

---

## Group: Neural Nexus Team
**Members:**  
- jchiluka2024@fau.edu  
- svilambi2024@fau.edu  
- tporachenu2024@fau.edu

---

## 1. Solution Overview

Neural Nexus steps in to promote healthier habits through smarter tech:  
A **Discord bot** powered by **Generative AI** logic and fueled by a dynamic **CSV-driven knowledge base**.  
The bot transforms simple greetings and fruit queries into inspiring, educational, and interactive experiences.

**Key Features:**
- 🌟 Personalized greetings based on detected user mood.
- 🍎 Rich, detailed health benefits for over 20 fruits.
- 🧠 Intelligent keyword matching (even partial and case-insensitive).
- 🌱 Lifestyle suggestions aligned with wellness goals.
- 🔮 (Future-ready) Dynamic fruit recommendations based on user health needs.

**Operational Flow:**
1. User sends a message (e.g., "hello" or "what are the benefits of mango?").
2. Bot's Matching Engine consults the `BotRules2` knowledge base (CSV).
3. Tailored response is generated and posted back in real-time.

---

## 2. Requirement Analysis

### Functional Requirements:
| Requirement | Priority | Complexity | Outcome | GenAI Automation |
|:---|:---|:---|:---|:---|
| Respond to greetings with friendly messages | High | Low | Personalized replies | Prompt-based generation |
| Provide fruit benefits upon query | High | Medium | Detailed nutritional info | CSV + prompt-curated text |
| Handle partial/fuzzy/case-insensitive matching | High | Medium | Robust matching | Input normalization + fuzzy lookup |
| Dynamic updating of knowledge base (future) | Medium | Medium | Live rule updates | CSV reload mechanism (future) |
| Log user queries for future improvement | Medium | Low | User insights | Simple logging |
| Suggest fruits based on user-stated goals (future) | Low | High | Personalized health recommendations | ML pipeline (future) |

### Non-Functional Requirements:
| Requirement | Priority | Complexity | Outcome | How Addressed |
|:---|:---|:---|:---|:---|
| Sub-second response time | High | Low | Seamless UX | Efficient local CSV lookup |
| Lightweight and scalable | High | Medium | Easy multi-server deployment | Minimalist architecture (Discord.py, Pandas) |
| Easy rule updates | High | Low | Maintainable knowledgebase | Externalized CSV |
| Friendly, professional tone | Medium | Low | Positive experience | Curated prompt outputs |
| Secure credential handling | High | Medium | Prevent token leaks | Environment variables |

---

## 3. Solution Architecture

**Modular System Overview:**

- **User Message** ➔ Neural Nexus Bot (`discord.py`)
- **Bot** ➔ Matching Engine (`botengine.py`)
- **Matching Engine** ➔ Searches KnowledgeBase (`context.py`)
- **Response Generation** ➔ SimpleBrain (`simplebrain.py`)
- **Optional Future Module** ➔ Suggest Healthy Habits (ML)

![image](https://github.com/user-attachments/assets/66452f9e-2af5-4a80-b18c-bef3bd5d3cc0)

> 📦 Logging Module records user queries for analysis.

---

## 4. System Modeling

### Sequence Diagram
- **User** sends a message.
- **Neural Nexus Bot** receives and forwards to **Matching Engine**.
- **Matching Engine** queries **KnowledgeBase (CSV)**.
- **Bot** responds back to the user.

### Class Diagram
- `DiscordBot` → Communicates with users via Discord.
- `MatchingEngine` → Processes and matches inputs.
- `KnowledgeBase` → Manages fruit knowledge rules.
- `SimpleBrain` → Crafts friendly greeting and health responses.

---

## 5. Prototype Implementation Plan

| Step | Description |
|:---|:---|
| 1 | Install Python 3.11+, `discord.py`, `pandas` |
| 2 | Secure Discord bot token in `.env` |
| 3 | Initialize bot (`bot-1.py`) |
| 4 | Process modular matching (`botengine.py`) |
| 5 | Query knowledgebase (`context.py`) |
| 6 | Generate response (`simplebrain.py`) |
| 7 | (Optional) Log user queries |
| 8 | (Future) Dockerize bot for hosting |

**Frameworks and Libraries:**
- `discord.py`
- `pandas`
- `python-dotenv`
- `fuzzywuzzy` (optional for fuzzy matching)

**Automation Techniques:**
- Prompt-engineered CSV knowledgebase.
- Auto-normalization and flexible matching logic.
- Modular, low-code expansion structure.

---

## 6. Experimental Prototype

| Deliverable | Link/Status |
|:---|:---|
| GitHub Repository | [GitHub Repo](https://github.com/Nchiluka18/Final_project/blob/main/README.md) |
| Live Bot | Private testing phase |

---

### Automation Successes:
- Automated knowledgebase generation (fruits, greetings) via prompt pipelines.
- Rule matching automation with input normalization and fuzzy matching.
- Modular architecture separating logic, matching, and response formatting.
- Knowledge rules externalized from code for easy updates (CSV).

---

## 7. Future Enhancements

- Dynamic fruit recommendations based on user health needs (ML-based).
- Live auto-reloading of updated CSV files without restarting the bot.
- Dynamic image generation for fruit benefit posters using multimodal AI (e.g., DALL·E 3).

---

## 📄 Conclusion

Neural Nexus demonstrates the powerful synergy between Generative AI techniques and software development lifecycles.  
We showcased how thoughtful GenAI integration can accelerate SDLC phases while maintaining flexibility and scalability by automating the design, knowledge base creation, response generation, and system modeling.  
This project lays a strong foundation for future enhancements, pushing toward even greater levels of automation and intelligent user interaction.

---

