#!/bin/bash

git config --global user.name "juliamacedo63"
git config --global user.email "julia.macedo63@aluno.ifce.edu.br"

cp /home/aluno/.ssh/20231321000057 /home/aluno/.ssh/id_ed25519
cp /home/aluno/.ssh/20231321000057.pub /home/aluno/.ssh/id_ed25519.pub

chmod 600 /home/aluno/.ssh/id_ed25519
chmod 644 /home/aluno/.ssh/id_ed25519.pub

echo "Configuração"
