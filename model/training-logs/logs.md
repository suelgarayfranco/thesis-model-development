# LOGS

- Model: T5-base-spanish
- Dataset Type: only-trees
- Dataset: preprocessed-dataset-only-trees-es
- Batch size: 4
- Epochs: 3
- Logging steps: 20
- Logs json: [LOGS](t5s-ot-logs.json)
- Ejemplos:
    * _Entrada_: "polinomio de grado 3 y coeficientes fraccionarios" _Salida_: SUM MUL VF POW x 3 E MUL VF POW x 2
    * _Entrada_: "polinomio de grado dos" _Salida_: SUM VF MUL VF x E MUL VF POW x 2 E
    * _Entrada_: "polinomio de segundo grado" _Salida_: SUM MUL VD POW x 2 E MUL VD x E VD
    * _Entrada_: "polinomio de grado 9 con termino independiente y principal" _Salida_: SUM MUL VR POW x 9 E MUL VR POW x 7 E M


- Model: T5-base-spanish
- Dataset Type: only-trees
- Dataset: preprocessed-dataset-only-trees-es
- Batch size: 4
- Epochs: 8
- Logging steps: 20
- Logs json: [LOGS](t5s-ot-8ep-logs.json)
- Ejemplos:
    * _Entrada_: "polinomio de grado tres y coeficientes fraccionarios" _Salida_: SUM MUL VF POW x 3 E MUL VF x E VF E
    * _Entrada_: "polinomio de grado dos" _Salida_: SUM VN NEG MUL VN x E NEG MUL VN POW x 2 E E
    * _Entrada_: "polinomio de segundo grado" _Salida_: SUM MUL VD POW x 2 E MUL VD x E VD E
    * _Entrada_: "polinomio de grado 9 con termino independiente y principal" _Salida_: SUM NEG MUL VN POW x 9 E NEG MUL VN POW x 8 E NEG MUL VN POW x 7 E NEG MUL VN POW x 6 E NEG MUL VN POW x 5 E NEG MUL VN POW x 4 E NEG MUL VN POW x 3 E NEG MUL VN POW x 2 E MUL VN x E NEG VN E
    * _Entrada_: "sistema de 2 ecuaciones" _Salida_: CASES EQ SUM MUL VN x E NEG MUL VN y E E VF EQ SUM MUL VN x E NEG MUL VF y E E VN E
    * _Entrada_: "sistema de ecuaciones con 3 variables" _Salida_: CASES EQ SUM MUL VF y E NEG MUL VN z E NEG MUL VF x E E VF EQ SUM NEG MUL VF y E NEG MUL VF x E E VF E

---

- Model: T5-base-spanish
- Dataset Type: latex
- Dataset: preprocessed-dataset-latex
- Batch size: 4
- Epochs: 5
- Logging steps: 100
- Logs json: [LOGS](train-latex-logs.json)
- Test logs: {'eval_loss': 0.2508312165737152, 'eval_runtime': 70.232, 'eval_samples_per_second': 2.036, 'eval_steps_per_second': 0.513, 'epoch': 5.0}

---
- Model: T5-base-spanish
- Dataset Type: latex-ner
- Dataset: preprocessed-dataset-latex-ner
- Batch size: 4
- Epochs: 5
- Logging steps: 100
- Logs json: [LOGS](train-latex-ner-logs.json)
- Test logs: 

---

- Model: T5-base-spanish
- Dataset Type: latex-trees
- Dataset: preprocessed-dataset-latex-trees
- Batch size: 4
- Epochs: 5
- Logging steps: 100
- Logs json: [LOGS](train-latex-trees-logs.json)
- Test logs: {'eval_loss': 0.11675252765417099, 'eval_runtime': 49.7096, 'eval_samples_per_second': 2.877, 'eval_steps_per_second': 0.724, 'epoch': 5.0}

---

- Model: T5-base-spanish
- Dataset Type: complete
- Dataset: preprocessed-dataset-complete
- Batch size: 4
- Epochs: 5
- Logging steps: 100
- Logs json: [LOGS](train-latex-trees-logs.json)
- Test logs: {'eval_loss': 0.10755975544452667, 'eval_runtime': 64.0738, 'eval_samples_per_second': 2.232, 'eval_steps_per_second': 0.562, 'epoch': 5.0}

