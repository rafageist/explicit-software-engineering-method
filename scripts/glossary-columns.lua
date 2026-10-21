-- Typeset Markdown divs with class "glossary" in two columns in LaTeX output.
-- Other output formats keep the div content unchanged.
function Div(el)
  if not el.classes:includes("glossary") then
    return nil
  end
  if not FORMAT:match("latex") then
    return el.content
  end
  local blocks = { pandoc.RawBlock("latex", "\\begin{multicols}{2}\\small") }
  for _, block in ipairs(el.content) do
    table.insert(blocks, block)
  end
  table.insert(blocks, pandoc.RawBlock("latex", "\\end{multicols}"))
  return blocks
end
