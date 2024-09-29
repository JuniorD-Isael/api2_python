# API2 Python

Esta é a API2 desenvolvida com FastAPI para processamento de imagens e identificação de marcas usando OCR.

## Funcionalidades

- Recebe uma imagem através de um endpoint.
- Converte a imagem para escala de cinza.
- Utiliza o Tesseract para extrair texto da imagem.
- Retorna o nome da marca detectada.

## Endpoints

### `POST /process-image`

**Descrição**: Processa a imagem enviada e retorna o nome da marca.

**Parâmetros**:

- `file`: O arquivo de imagem a ser processado.

**Resposta**:

```json
{
  "brandName": "Nome da Marca Detectada"
}
```

## Instalação

Para instalar as dependências, use o Poetry:

```bash
poetry install
```

## Execução

Para iniciar a API, execute:

```bash
uvicorn main:app --reload
```

## Dependências

- FastAPI
- Uvicorn
- pytesseract
- Pillow
- python-multipart

