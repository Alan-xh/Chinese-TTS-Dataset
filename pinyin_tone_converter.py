from pypinyin import Style
from pypinyin.style import convert

text = "Nà shì lìzhēng shàngyóu de yī zhǒng shù，bǐzhí de gàn，bǐzhí de zhī．"

# 加上 strict=False 即可正确运行
result = convert(text, style=Style.TONE3, strict=False)

print(result)
# 输出: Na4 shi4 li4zheng1 shang4you2 de1 yi1 zhong3 shu4，bi3zhi2 de1 gan4，bi3zhi2 de1 zhi1．