#!/bin/bash

# Função para criar diretórios e arquivos
create_structure() {
    base_path=$1
    declare -A structure=$2

    for dir in "${!structure[@]}"; do
        # Cria diretórios dentro de 'base_path'
        dir_path="$base_path/$dir"
        if [ ! -d "$dir_path" ]; then
            mkdir -p "$dir_path"
            echo "Diretório criado: $dir_path"
        fi

        # Cria arquivos dentro do diretório
        files="${structure[$dir]}"
        for file in $files; do
            file_path="$dir_path/$file"
            if [ ! -f "$file_path" ]; then
                touch "$file_path"
                echo "# $file - Arquivo criado automaticamente." > "$file_path"
                echo "Arquivo criado: $file_path"
            fi
        done
    done
}

# Caminho base para criação da estrutura (diretório 'api')
base_path="api"  # Definindo diretamente a pasta 'api'

# Definindo a estrutura de diretórios e arquivos
declare -A api_structure
api_structure=(
    ["migrations"]=" "
    ["views"]="__init__.py colaborador.py regimejornada.py usuario.py gerente.py colaborador.py resumo_jornada.py"
    ["serializers"]="__init__.py colaborador.py regimejornada.py usuario.py gerente.py colaborador.py resumo_jornada.py"
    ["admin"]="__init__.py colaborador.py regimejornada.py usuario.py gerente.py colaborador.py resumo_jornada.py"
    ["urls"]="__init__.py colaborador.py regimejornada.py usuario.py gerente.py colaborador.py resumo_jornada.py"
    ["permissions"]="todos.py"
)

# Criação da estrutura na pasta 'api'
create_structure "$base_path" api_structure

echo "Estrutura de diretórios e arquivos criada com sucesso dentro da pasta 'api'."
