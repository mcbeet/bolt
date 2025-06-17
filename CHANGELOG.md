# Changelog

<!--next-version-placeholder-->

## v0.49.2 (2025-06-17)

### Fix

* Make sure that load_prelude() keeps returning the same thing for the same file ([`e0bb5b8`](https://github.com/mcbeet/bolt/commit/e0bb5b820c2d364db04480b2fb9a6539b4302f77))

## v0.49.1 (2024-07-22)

### Fix

* Allow singular module folder ([`8e7de60`](https://github.com/mcbeet/bolt/commit/8e7de601a355cd76af46873d6f8db0317f2ecacb))

## v0.49.0 (2024-07-22)

### Feature

* Update beet and mecha ([`d55c37d`](https://github.com/mcbeet/bolt/commit/d55c37d6b1de4d997d2481f89c08d85f240695f4))

## v0.48.0 (2024-04-29)

### Feature

* Version 1.20.5 ([`959af66`](https://github.com/mcbeet/bolt/commit/959af66694d73442ce84a420d314b81720526716))

## v0.47.2 (2024-03-29)

### Fix

* Missed a file in previous commit ([`d9f27f5`](https://github.com/mcbeet/bolt/commit/d9f27f53bb7358cb59b9a37dc59e242efa550eeb))

## v0.47.1 (2024-03-29)

### Fix

* Interpolation for item_slots ([`2a8f9e0`](https://github.com/mcbeet/bolt/commit/2a8f9e0de038829fafdad234d44713db39fa0286))

## v0.47.0 (2024-02-23)

### Feature

* Fuse with statements across if statements ([`d93140a`](https://github.com/mcbeet/bolt/commit/d93140a587eb504bf99a3a5dac44dd7694edec70))
* Fuse with statements ([`d60f460`](https://github.com/mcbeet/bolt/commit/d60f460298955b17ab33efa6e3a17551bd401178))
* Refactor with statements ([`6770dc9`](https://github.com/mcbeet/bolt/commit/6770dc95bf76ad35dbbc8a7d89d80695282c70ea))
* Add basic loop overloading ([`497502a`](https://github.com/mcbeet/bolt/commit/497502a1fac66306313d8cb51d802214f4bcd0b2))

## v0.46.0 (2024-02-20)

### Feature

* Add chained comparison ([`0cc5da8`](https://github.com/mcbeet/bolt/commit/0cc5da8369b5774bd73cb6d249c5545cc95b0a13))

## v0.45.0 (2024-01-17)

### Feature

* Make it possible to use variable names that conflict with commands ([`f19ae15`](https://github.com/mcbeet/bolt/commit/f19ae159e3d47e33d1bff89f40828167c7ad726c))

## v0.44.1 (2024-01-17)

### Fix

* Share walk_location_hierarchy with mecha ([`973f3c1`](https://github.com/mcbeet/bolt/commit/973f3c136ce3d7cf0a27c0c3e98a54fb69b82c9f))
* Compat with mecha.contrib.json_files when it comes before bolt ([`430d488`](https://github.com/mcbeet/bolt/commit/430d4881812237ff797fe7d4499a008a9c65cb3c))

## v0.44.0 (2023-12-07)

### Feature

* Trigger rebind on set attribute ([`ed97089`](https://github.com/mcbeet/bolt/commit/ed9708942c23448c3e3297e19a48230f827d58ec))
* Expose minimal context info in sandbox ([`3c839a0`](https://github.com/mcbeet/bolt/commit/3c839a0b5f32e60dac774ac81ae851202ded6d73))

### Fix

* Fuse with statements in codegen ([`a7e9edf`](https://github.com/mcbeet/bolt/commit/a7e9edf1a6a2d1a86e76de49aca3908cfd9987df))
* Refactor codegen to use a statement tree ([`53a4ba9`](https://github.com/mcbeet/bolt/commit/53a4ba9b8bb4a46173246d0f26d551277f8a3989))
* Allow accumulator override ([`493c371`](https://github.com/mcbeet/bolt/commit/493c37169065694bbf62c69702ff5e50c86d08f1))

## v0.43.0 (2023-12-06)

### Feature

* Add codegen cli command ([`4e7db00`](https://github.com/mcbeet/bolt/commit/4e7db009930e93596d6ceea327e417cb60998c58))
* Update to 1.20.3 ([`e0c2f11`](https://github.com/mcbeet/bolt/commit/e0c2f117905f3c126a3df920ceb06d3b7c66c059))

## v0.42.0 (2023-12-02)

### Feature

* Update deps ([`fcc4bde`](https://github.com/mcbeet/bolt/commit/fcc4bdea6c582933e905f4e3ee30c394eb607d1b))

## v0.41.1 (2023-11-28)

### Fix

* Early inverse binding for else condition ([`44a6dbf`](https://github.com/mcbeet/bolt/commit/44a6dbf3bdda67288c00417d364e3384e92d26b3))

## v0.41.0 (2023-11-13)

### Feature

* Class kwargs ([`c6d6c94`](https://github.com/mcbeet/bolt/commit/c6d6c94591322807b8fea6233e785b0f05666c6a))

## v0.40.0 (2023-10-31)

### Feature

* Asset module ([`3e3fa7d`](https://github.com/mcbeet/bolt/commit/3e3fa7d810595f7bc0dc8c1691e54d31c7ecc5aa))

## v0.39.2 (2023-10-30)

### Fix

* Update mecha ([`5bac0ec`](https://github.com/mcbeet/bolt/commit/5bac0ec7539a1e85884d92e42db85b56447be09a))

## v0.39.1 (2023-10-30)

### Fix

* Update deps ([`3a160b1`](https://github.com/mcbeet/bolt/commit/3a160b1418f7c004b16516008cc000a9234933f0))

## v0.39.0 (2023-10-28)

### Feature

* Refactor non-function root ([`b74f756`](https://github.com/mcbeet/bolt/commit/b74f756229f2ba4f22a09c00caa512aebf810a1e))

## v0.38.5 (2023-10-15)

### Fix

* Import from overlay fall back to main pack ([`ebe2434`](https://github.com/mcbeet/bolt/commit/ebe243453c108ac315b9c5cdd7fa0e14c9b3e2fa))

## v0.38.4 (2023-10-15)

### Fix

* Distinct preludes for overlays ([`5f858e5`](https://github.com/mcbeet/bolt/commit/5f858e558fec97d12fbf9436f1ac81006e1deb1a))

## v0.38.3 (2023-10-15)

### Fix

* Clear modules from overlays ([`b98f18d`](https://github.com/mcbeet/bolt/commit/b98f18d1401392d22b807eef1695f9b94db885f8))

## v0.38.2 (2023-10-14)

### Fix

* Compile memo with proper nesting ([`a88de67`](https://github.com/mcbeet/bolt/commit/a88de679eb307d9595366a2104ae659652cd70ed))

## v0.38.1 (2023-10-10)

### Fix

* Handle anonymous macro invocations ([`6d4d5c0`](https://github.com/mcbeet/bolt/commit/6d4d5c094caeae4fae79445fc5106cafea968a0d))

## v0.38.0 (2023-10-09)

### Feature

* Update deps ([`9a42907`](https://github.com/mcbeet/bolt/commit/9a42907cfad7fb5ed4eec202acd0e53f29c93e43))

## v0.37.0 (2023-08-03)

### Feature

* Bump mecha to support backslash continuations ([`3d25461`](https://github.com/mcbeet/bolt/commit/3d2546147b5be2438281ce44110444805ec25d05))

## v0.36.0 (2023-06-07)

### Feature

* Delegate to mecha for nested locations without formatting ([`b5b753e`](https://github.com/mcbeet/bolt/commit/b5b753e80a80adda916976daf17aa0660590e83a))

### Fix

* Take whitespace into account for interpolation ([`3f59e63`](https://github.com/mcbeet/bolt/commit/3f59e6384bac384c46b9718cdf115fe7d994373d))

## v0.35.0 (2023-05-20)
### Feature
* Nested locations ([`a7fe760`](https://github.com/mcbeet/bolt/commit/a7fe760d552630d5528522f332bba211d4006233))

## v0.34.0 (2023-05-18)
### Feature
* Add runtime nesting info ([`2100ee7`](https://github.com/mcbeet/bolt/commit/2100ee773026b6dc353fb8d753034c6db09a0b9f))

## v0.33.2 (2023-04-26)
### Fix
* Don't handle docstrings behind subcommands ([`2fd8c25`](https://github.com/mcbeet/bolt/commit/2fd8c256cf9272fea7b908b654f0ef25d2118c13))

## v0.33.1 (2023-04-25)
### Fix
* Only rewrite vanilla return inside function scope ([`e874832`](https://github.com/mcbeet/bolt/commit/e874832ef13af24b69382c6d84a2a4fdaeac3fe3))

## v0.33.0 (2023-04-25)
### Feature
* Handle vanilla return ([`90c3f54`](https://github.com/mcbeet/bolt/commit/90c3f541c66af7e626f9bab83e4cd35ed71f4d05))

## v0.32.0 (2023-04-25)
### Feature
* Update mecha ([`fba874e`](https://github.com/mcbeet/bolt/commit/fba874e345e655231cf1a66951c78b719fbb68c1))

## v0.31.0 (2023-02-19)
### Feature
* Add prelude option ([`b0937e0`](https://github.com/mcbeet/bolt/commit/b0937e06affd62e8f358638358ce2797644d36e7))

## v0.30.1 (2023-02-15)
### Fix
* Properly track del statement semantics ([`66c543f`](https://github.com/mcbeet/bolt/commit/66c543fd82902ed7cbf7e04e6a0b57a45715c0bd))

## v0.30.0 (2023-02-09)
### Feature
* Macro subcommands ([`5db484e`](https://github.com/mcbeet/bolt/commit/5db484ef754bbd5eaeea0c16574ecc23e160a490))

## v0.29.0 (2023-02-06)
### Feature
* Update 1.19 ([`0a8ca58`](https://github.com/mcbeet/bolt/commit/0a8ca580f4e3b155154fd8714ddb6ccc4c13121f))

## v0.28.0 (2023-02-05)
### Feature
* Error when using unsupported statements in memo ([`e57c845`](https://github.com/mcbeet/bolt/commit/e57c845f28cd40669ace582dcb2f404cf384582d))

## v0.27.0 (2023-02-05)
### Feature
* Restore memo bindings ([`48c5fe9`](https://github.com/mcbeet/bolt/commit/48c5fe996ff5a575bf50b5bf5f572320fedfb39e))

## v0.26.0 (2023-02-02)
### Feature
* Add type annotations ([`a3970f1`](https://github.com/mcbeet/bolt/commit/a3970f1a61668c5cf772ad24eacd7a835aa1824e))

## v0.25.0 (2023-02-01)
### Feature
* Add docstrings ([`c1c1488`](https://github.com/mcbeet/bolt/commit/c1c1488d60d58abc2a66d8cd02b671831bbf4473))

## v0.24.1 (2023-02-01)
### Fix
* Update pyright ([`24120a9`](https://github.com/mcbeet/bolt/commit/24120a963b476676391a51fa25350a6a06225469))

## v0.24.0 (2023-02-01)
### Feature
* Atlas ([`8703186`](https://github.com/mcbeet/bolt/commit/87031867ab7ce7014f88ef30e129cf1b115f5945))

## v0.23.0 (2023-01-31)
### Feature
* Add memo and a bunch of tweaks ([`77326b7`](https://github.com/mcbeet/bolt/commit/77326b7056a038743a1f20511ae565cacbc15f10))

## v0.22.0 (2022-12-04)
### Feature
* Refactor identifier tracing with proper lexical scope abstraction ([`2f60bd4`](https://github.com/mcbeet/bolt/commit/2f60bd43c8affc2747c56e2d4dd4045e45561677))

## v0.21.1 (2022-12-03)
### Fix
* Default empty arguments for AstFunctionSignature ([`6c79443`](https://github.com/mcbeet/bolt/commit/6c794431fe5b4c826dea8cae54a63d8c54838ad9))

## v0.21.0 (2022-11-23)
### Feature
* Add bolt.contrib.defer ([`6a0527f`](https://github.com/mcbeet/bolt/commit/6a0527f4696081a168a5adbfbb6a5f74d4853c4b))
* Add CommandCollector ([`a07cedd`](https://github.com/mcbeet/bolt/commit/a07cedd2e4636b50494ff7cdd914050d194fe922))
* Disable mecha.contrib.inline_function_tag by default ([`a9bf8bf`](https://github.com/mcbeet/bolt/commit/a9bf8bfe3d7bb39d767c204e4f06a80cc4133d78))

## v0.20.1 (2022-10-26)
### Fix
* Reset token generator after discarding builtin identifier in interpolation ([`37f74bc`](https://github.com/mcbeet/bolt/commit/37f74bc8f9fbf60b0493bf8e158be678ced5f272))

## v0.20.0 (2022-10-24)
### Feature
* Interpolate advancement predicate ([`e4338b0`](https://github.com/mcbeet/bolt/commit/e4338b0f4004601daf9c86b169a3771f876cff16))

### Fix
* Refactor interpolation ([`44c2d0e`](https://github.com/mcbeet/bolt/commit/44c2d0ed74c8100698fa75931df626c96329b820))

## v0.19.3 (2022-10-19)
### Fix
* Reset generator to prevent dropping tokens ([`6551578`](https://github.com/mcbeet/bolt/commit/65515786d6a941a2f4e94c4e8932c0dc90faa14f))
* Update deps ([`1a00f20`](https://github.com/mcbeet/bolt/commit/1a00f208fce10a37e2ef9003d478b8dddce30d73))

## v0.19.2 (2022-10-04)
### Fix
* Reported 0 errors message ([`16e64b7`](https://github.com/mcbeet/bolt/commit/16e64b77d5516fa04687f156ace6a4ee050be95b))
* Proper error for statements used as subcommands ([`647b1c6`](https://github.com/mcbeet/bolt/commit/647b1c6685f5653bf34fdc87fab7ce2a7edc6fba))

## v0.19.1 (2022-09-12)
### Fix
* Add error for non-default args following default args ([`2af9854`](https://github.com/mcbeet/bolt/commit/2af9854d91818804b642ffe2a7b625a6412665ec))

## v0.19.0 (2022-09-11)
### Feature
* Update compilation priority depending on execution order ([`d6aa9ec`](https://github.com/mcbeet/bolt/commit/d6aa9ecf55027e411889459986d79123239ec81b))

## v0.18.1 (2022-09-11)
### Fix
* Update deps ([`89b37c1`](https://github.com/mcbeet/bolt/commit/89b37c1b1d5cac57b1fdc1f5bef0971c41dd3e1b))

## v0.18.0 (2022-09-11)
### Feature
* Positional-only, variadic, keyword-only, and variadic keyword arguments ([`6413593`](https://github.com/mcbeet/bolt/commit/64135935c8f54dbde20807cba6481202dbf394e6))

## v0.17.7 (2022-08-16)
### Fix
* Update beet ([`c494033`](https://github.com/mcbeet/bolt/commit/c494033639d389fb6a3165ddefa04d8dc3c4a08e))

## v0.17.6 (2022-08-12)
### Fix
* Import parser properly delegates to resource location parser ([#37](https://github.com/mcbeet/bolt/issues/37)) ([`a971b07`](https://github.com/mcbeet/bolt/commit/a971b07e15d7382216f90c51233e3e7762a05b47))

## v0.17.5 (2022-08-06)
### Fix
* Builtins used as dict keys are now unquoted strings ([`015ff65`](https://github.com/mcbeet/bolt/commit/015ff657229b02d5930b0a5756e95d515e8df70e))
* Only allow call expressions on builtins for interpolation ([`0526a85`](https://github.com/mcbeet/bolt/commit/0526a85af232e05255e24e07a43ee720a1bb87f4))

## v0.17.4 (2022-08-06)
### Fix
* Truncate primary expression for interpolation ([`014802f`](https://github.com/mcbeet/bolt/commit/014802fcf98314b270868503a8f4bca1a3429d31))

## v0.17.3 (2022-07-25)
### Fix
* Enable interpolation for uuid ([`39cc462`](https://github.com/mcbeet/bolt/commit/39cc4624f555874808c629000c260c2feefbb5b4))

## v0.17.2 (2022-07-25)
### Fix
* Enable interpolation for game_profile argument ([`e844f49`](https://github.com/mcbeet/bolt/commit/e844f49906fa693edf9fe509427211b2b01ad39d))

## v0.17.1 (2022-07-21)
### Fix
* Only allow imports and macros directly at scope level ([`2f069bd`](https://github.com/mcbeet/bolt/commit/2f069bd6ae7e689605303fb99fa272bdc4b17e36))

## v0.17.0 (2022-07-20)
### Feature
* Add bolt classes ([`71c1162`](https://github.com/mcbeet/bolt/commit/71c1162c99c61eb747573a370646f80b787f95f5))

## v0.16.0 (2022-07-17)
### Feature
* Make modules lazy by default ([`370a759`](https://github.com/mcbeet/bolt/commit/370a7596d0a5764dfe0c2ce5e553483f8728ab60))

## v0.15.0 (2022-07-17)
### Feature
* Add raw strings ([`e24d772`](https://github.com/mcbeet/bolt/commit/e24d7721ddd8e708735f7e3b16c50b81cbfb4a89))

## v0.14.0 (2022-07-17)
### Feature
* Ergonomic improvements for dicts without quotes ([`18c747e`](https://github.com/mcbeet/bolt/commit/18c747e74aa2500fbb47414d0bc4ea24a3af04a1))

## v0.13.0 (2022-07-17)
### Feature
* Add raise statement ([`d5654a5`](https://github.com/mcbeet/bolt/commit/d5654a58c95ea326ff01da92b88bfd2e29e48b6c))
* Add proc macro ([`97e1bea`](https://github.com/mcbeet/bolt/commit/97e1beadb033de13453ef9deee1c290bdd730f4e))

## v0.12.2 (2022-07-15)
### Fix
* Update beet ([`a4f2f97`](https://github.com/mcbeet/bolt/commit/a4f2f97feef98d9c9f624ffc82a3d8e5ff282337))

## v0.12.1 (2022-07-15)
### Fix
* Memoize command trees ([`8c8911a`](https://github.com/mcbeet/bolt/commit/8c8911ae16e3c2829c0e33dbc3a2fab248505b81))
* Make command tree updates lazy ([`ec17f74`](https://github.com/mcbeet/bolt/commit/ec17f7479072a63e8e81a8c17163d69c680a9b5e))
* Minor tweaks ([`35a537e`](https://github.com/mcbeet/bolt/commit/35a537e9a4a6e471a17cfc99b8776bdc3135fd88))

## v0.12.0 (2022-07-13)
### Feature
* Add macro imports ([`e8ca750`](https://github.com/mcbeet/bolt/commit/e8ca750c6664ffa610b09c17d00cb7f9eed445c8))

## v0.11.0 (2022-07-10)
### Feature
* Turn module manager into a mapping ([`3c486eb`](https://github.com/mcbeet/bolt/commit/3c486eb6d9ce6c9a47ec16c14342fa98db6fbfd7))
* Extract module manager from runtime ([`20e7499`](https://github.com/mcbeet/bolt/commit/20e74995ab2b44505a494e352f94d1c756ba0ec6))
* Make it possible to run the lazy plugin multiple times ([`87df070`](https://github.com/mcbeet/bolt/commit/87df070d2f528a95c06b14fb2a8b3e019e80651c))

## v0.10.0 (2022-07-09)
### Feature
* Working macro and tests ([`a0ddfba`](https://github.com/mcbeet/bolt/commit/a0ddfbab5a46b173ec8a0bd46f8e78c76a098c85))
* Start working on macro ([`e3bbb3e`](https://github.com/mcbeet/bolt/commit/e3bbb3e83dd2f60df2a4f8ca848782b7a83a2c84))

### Fix
* Update mecha ([`e6c77e9`](https://github.com/mcbeet/bolt/commit/e6c77e9d495e7de8dcc3326ea15c2edc767249f7))

## v0.9.1 (2022-07-02)
### Fix
* Allow ast node interpolation directly ([`ffa076e`](https://github.com/mcbeet/bolt/commit/ffa076efa635be32c735371e2761da954385abbf))

## v0.9.0 (2022-06-24)
### Feature
* Add bolt.contrib.lazy ([`c9f12f3`](https://github.com/mcbeet/bolt/commit/c9f12f360c70ca031acfe5f9b2f0213bc7c3fdff))
* Add compiled module execution hooks ([`0a91936`](https://github.com/mcbeet/bolt/commit/0a91936a8172ad7b2b246c38b931cac8da6a27d2))

### Fix
* Minor visual changes ([`0ab3519`](https://github.com/mcbeet/bolt/commit/0ab35197e9d8f8532c39faf4b2a03caa938077bc))

## v0.8.2 (2022-06-24)
### Fix
* Remove leftover extern plugin ([`42cc659`](https://github.com/mcbeet/bolt/commit/42cc6590bfef34cc4573ed8d2fe8404cf26c9f34))

## v0.8.1 (2022-06-18)
### Fix
* Update deps for new snapshot settings ([`6739b2b`](https://github.com/mcbeet/bolt/commit/6739b2bb0d4521de90e6162f40033d37b2550fcd))

## v0.8.0 (2022-06-18)
### Feature
* Add context managers ([`38e614e`](https://github.com/mcbeet/bolt/commit/38e614e8d38d1c62af019f2b5f08a78cff22ed0b))

## v0.7.2 (2022-06-17)
### Fix
* Only restrict builtins when sandbox is active ([`8eefb0c`](https://github.com/mcbeet/bolt/commit/8eefb0cf1f5d6f3a6b0e472ffb1da0e6b60ba5e7))

## v0.7.1 (2022-06-15)
### Fix
* Track bolt version in cached ast ([`1e5d2d1`](https://github.com/mcbeet/bolt/commit/1e5d2d119872397dadac006c18b2c3909ccf6496))

## v0.7.0 (2022-06-15)
### Feature
* Support decorators ([`3e8f60b`](https://github.com/mcbeet/bolt/commit/3e8f60bf9b7e9c74b631bdf689f4370f76f37766))

### Fix
* Change prefix of codegen variables ([`f9cc901`](https://github.com/mcbeet/bolt/commit/f9cc9013ba1dd1333a2b5a199c29c84d054e15be))

## v0.6.0 (2022-05-27)
### Feature
* Add bolt.contrib.debug_codegen ([`d504b00`](https://github.com/mcbeet/bolt/commit/d504b00867bf22770708e6eeb6190ed790f0a483))

## v0.5.1 (2022-05-27)
### Fix
* Handle uppercase python imports ([`a5e50e0`](https://github.com/mcbeet/bolt/commit/a5e50e0173b47310db43b6915d31b707b7218c3a))

## v0.5.0 (2022-05-06)
### Feature
* Iterable/mapping unpacking in json/nbt interpolation ([`32acee0`](https://github.com/mcbeet/bolt/commit/32acee0e8bbf2c831fa48c30595b63ed61f1de40))
* Unpack field for interpolation node ([`b2f6dd7`](https://github.com/mcbeet/bolt/commit/b2f6dd7017afe5c7ebc4c530f152b666c7557ba1))

### Fix
* Converter for json object ([`825f077`](https://github.com/mcbeet/bolt/commit/825f077e14bafdf719f4f488347714b5761886ac))

## v0.4.2 (2022-05-02)
### Fix
* Update mecha to fix indent bug ([`006a57a`](https://github.com/mcbeet/bolt/commit/006a57a4ff0f0e99af106e235440c5c7b06f1f71))

## v0.4.1 (2022-05-01)
### Fix
* Leftover print ([`3731f2c`](https://github.com/mcbeet/bolt/commit/3731f2c071942d0e131f42432bbd165bdf4e602e))

## v0.4.0 (2022-05-01)
### Feature
* Update beet to allow bolt files outside of the data pack ([`5c0d58c`](https://github.com/mcbeet/bolt/commit/5c0d58c181a053c2c0090d9af8b6eb96b6bc54f8))

## v0.3.4 (2022-04-30)
### Fix
* Update mecha to handle nbtlib instances properly for interpolation ([`fce1766`](https://github.com/mcbeet/bolt/commit/fce1766807e588d5a7c75b7e4e407926c0bc164d))

## v0.3.3 (2022-04-30)
### Fix
* Use next_token ([`3fb3aab`](https://github.com/mcbeet/bolt/commit/3fb3aabae017862b89d29c2124d523f2fd0c0e3a))

## v0.3.2 (2022-04-30)
### Fix
* Proper check for final expressions ([`57bb1f1`](https://github.com/mcbeet/bolt/commit/57bb1f18b09bc7b9ab04079651668341262a462b))

## v0.3.1 (2022-04-29)
### Fix
* Make message interpolation final ([`b46b165`](https://github.com/mcbeet/bolt/commit/b46b1652ee78a3224911a7a57173c9f3f236244e))

## v0.3.0 (2022-04-29)
### Feature
* Allow nbt compound interpolation ([`b6f964f`](https://github.com/mcbeet/bolt/commit/b6f964fc16805bedc1d3be94a7d042acf4112551))

## v0.2.1 (2022-04-26)
### Fix
* Use BubbleException ([`c8ce2fb`](https://github.com/mcbeet/bolt/commit/c8ce2fb478fa35aff0cf768cdb320302cf123378))

## v0.2.0 (2022-04-25)
### Feature
* Setup project ([`50b4bea`](https://github.com/mcbeet/bolt/commit/50b4beaf0faad49fad9785423378002d2bdd482a))
