# A Preliminary Study on EEG-fNIRS Indicators for Monitoring Emotional Attention and Fatigue

## Project Overview

![image](https://github.com/user-attachments/assets/0c403a7b-062b-47db-a46a-615660aa3908)


This project investigates the **neurophysiological mechanisms of attention and fatigue** under emotional stimuli using a **hybrid EEG-fNIRS system**. By employing an *Emotional Face-Word Stroop Task*, we analyze how congruency between facial expressions and emotional words modulates cognitive processes, and whether mental fatigue accumulates over time.

---

## Objectives

- Explore **EEG-based attention markers** (e.g., N2, P3, N450) under emotional Stroop conditions.
- Analyze **trial-based fatigue accumulation** using fNIRS HbO signals.
- Validate the potential for **real-time fatigue/attention monitoring** via multimodal neuroimaging.
- Identify interaction effects between emotional valence and semantic congruency.

---

## Experimental Setup

![image](https://github.com/user-attachments/assets/24cf764b-f46e-45d0-88be-2355f5bfd77f)

### Stimuli
- **YFaceDB**: Korean facial expression image dataset.
- Target emotions: *Happy*, *Sad*.
- Semantic words: Emotionally congruent or incongruent with faces.
- Total 4 conditions:
  - Happy-Congruent (HC)
  - Happy-Incongruent (HI)
  - Sad-Congruent (SC)
  - Sad-Incongruent (SI)

### Task Paradigm
- Trial design:
  - 1s visual stimulus
  - Mouse response (emotion selection)
  - Fixation cross (1–5s jittered)
- 40 trials per condition × 3 participants

---

## Data Acquisition

| Modality | Device | Channels | Sampling Rate |
|----------|--------|----------|----------------|
| EEG | Brain Products actiCHamp Plus | 32 | 1000 Hz |
| fNIRS | NIRSport2 (NIRx) | 16 | ~8 Hz (derived) |

- EEG referenced to FCz
- fNIRS optode pairs placed over PFC, STC, OC

---

## Data Preprocessing

<img width="188" alt="image" src="https://github.com/user-attachments/assets/d4fc7957-be5a-4ad3-9f35-8ffff1237d51" />

### EEG
- Bandpass filter: 1–40 Hz
- ICA (for eye/muscle artifact removal)
- Epoch: -200 to 1000 ms (baseline corrected)
- ERP extraction for each condition

<img width="188" alt="image" src="https://github.com/user-attachments/assets/34804e67-9e57-4cdc-8233-5d2513d74af8" />

### fNIRS
- Wavelet filtering (5-level decomposition)
- Modified Beer–Lambert Law (MBLL) → HbO/HbR
- Signal standardization across participants
- 10-trial window averaging (fatigue trend analysis)

---

## Analysis Pipeline

### Behavioral
- Accuracy and Reaction Time (RT)
- 2×2 ANOVA: Congruency × Emotion

### EEG (ERP)
- Component focus: N2 (conflict), P3 (decision), N450 (Stroop-specific)
- Congruency effect: SI > HI > HC ≈ SC in negative amplitude
- Topographical comparison across conditions

![image](https://github.com/user-attachments/assets/b9e5b779-d817-4499-a37a-0826324f8050)

### fNIRS (Fatigue)
- Channel-wise HbO changes over trials
- No significant linear trend (fatigue not induced)
- ANOVA: No effect of trial block on HbO

![image](https://github.com/user-attachments/assets/d385eae4-f7e4-4fe7-86f7-c4603d16478a)

---

## Key Results

| Measure | Finding |
|--------|---------|
| Accuracy | >96% across all conditions |
| RT | No significant difference (p > 0.1) |
| ERP (EEG) | SI condition shows strongest negativity (N2/N450) |
| HbO (fNIRS) | No consistent increase/decrease → no fatigue evidence |

---

## Limitations

- Small sample (N=3)
- Task difficulty too low to elicit cognitive fatigue
- Emotion induction via facial expression may be too weak
- Short stimulus duration (1s) may limit ERP clarity

---

## Future Directions

- **Increase task complexity**: block design or repetitive dual tasks
- **Larger participant pool** for statistical power
- **Integrate EEG-fNIRS features** into machine learning models
- Explore **longer emotional tasks** or **VR-based immersive stimuli**

---

## Directory Structure

- `analysis/`  
  Contains Python scripts and Jupyter notebooks for EEG/fNIRS signal processing and data analysis.

- `data/`  
  Stores raw and preprocessed experimental data, including EEG, fNIRS, and participant response files.

- `experiment/`  
  Includes the experiment program code and related stimulus presentation scripts.



