# Lectern snapshot

## Data pack

`@data_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 10,
    "description": ""
  }
}
```

### demo

`@function demo:load`

```mcfunction
say hello
```

`@function demo:tick`

```mcfunction
say demo:tick
execute as @e[tag=demo.entity] run say entity
```

### minecraft

`@function_tag minecraft:tick`

```json
{
  "values": [
    "demo:tick"
  ]
}
```
