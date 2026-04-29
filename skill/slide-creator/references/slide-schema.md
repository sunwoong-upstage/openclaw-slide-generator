# Slide JSON Schema

`generate_slides.py` accepts a JSON payload via stdin or `--input` flag.

## Top-level structure

```json
{
  "title": "Presentation Title",
  "subtitle": "Optional subtitle",
  "author": "Optional author name",
  "date": "Optional date string",
  "style": "modern",
  "lang": "ko",
  "slides": [
    { "type": "title", "content": "...", "speaker_notes": "..." },
    { "type": "heading", "content": "..." },
    { "type": "bullet", "items": ["..."], "speaker_notes": "..." },
    { "type": "code", "language": "python", "code": "..." },
    { "type": "image", "src": "url or path", "caption": "..." },
    { "type": "quote", "text": "...", "author": "..." },
    { "type": "two_col", "left": "...", "right": "..." },
    { "type": "table", "headers": [...], "rows": [[...]] },
    { "type": "closing", "content": "..." }
  ]
}
```

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | yes | Presentation title, shown on title slide and browser tab. |
| `subtitle` | string | no | Subtitle shown on title slide. |
| `author` | string | no | Author name, shown on title slide. |
| `date` | string | no | Date string, shown on title slide. |
| `style` | string | yes | Theme name: `modern`, `academic`, `playful`, `minimal`, `corporate`. |
| `lang` | string | yes | Language code for font loading. Common: `ko`, `en`, `ja`, `zh`. |
| `slides` | array | yes | Ordered list of slide objects. |

## Slide types

| `type` | Description | Fields |
|--------|-------------|--------|
| `title` | Title slide (first slide). | `content` (title), optional `speaker_notes`. |
| `heading` | Section divider with a big heading. | `content`. |
| `bullet` | Bullet list. | `items` (array of strings), optional `speaker_notes`. |
| `code` | Code block. | `language`, `code` (raw string), optional `speaker_notes`. |
| `image` | Full-slide image. | `src` (URL or relative path), optional `caption`, optional `speaker_notes`. |
| `quote` | Large centered quote. | `text`, optional `author`, optional `speaker_notes`. |
| `two_col` | Two-column text layout. | `left` (HTML/Markdown string), `right` (HTML/Markdown string), optional `speaker_notes`. |
| `table` | Data table. | `headers` (array), `rows` (array of arrays), optional `speaker_notes`. |
| `closing` | Final slide / CTA. | `content` (heading), optional `subtitle`, optional `speaker_notes`. |

## Example

```json
{
  "title": "Intro to OpenClaw",
  "style": "modern",
  "lang": "en",
  "slides": [
    { "type": "title", "content": "Intro to OpenClaw", "speaker_notes": "Welcome everyone." },
    { "type": "heading", "content": "What is OpenClaw?" },
    { "type": "bullet", "items": ["Open-source AI gateway", "Multi-channel messaging", "Skill ecosystem"], "speaker_notes": "Mention the community Discord." }
  ]
}
```