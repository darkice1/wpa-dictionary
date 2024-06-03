# wpa-dictionary

拆分大字典文件

```bash
SOURCE_FILE="rockyou.txt"; OUTPUT_PREFIX="rockyou_part"; MAX_SIZE=$((40*1024*1024)); gsplit -C $MAX_SIZE --numeric-suffixes=1 -a 4 $SOURCE_FILE $OUTPUT_PREFIX; for file in ${OUTPUT_PREFIX}*; do mv "$file" "$file.txt"; done
```
