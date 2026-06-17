-- WirePlumber Lua 规则：持久化声卡配置
-- 放到 ~/.config/wireplumber/main.lua.d/51-<name>.lua
--
-- 替换 alsa_card.pci-0000_00_1f.3 为你的声卡名（pactl list cards | grep '名称:'）
-- 替换 output:hdmi-stereo+input:analog-stereo 为目标配置（pactl list cards | grep '可用的配置'）

-- 持久化声卡 profile
rule = {
  matches = {
    {
      { "device.name", "equals", "alsa_card.pci-0000_00_1f.3" },
    },
  },
  apply_properties = {
    ["device.profile"] = "output:hdmi-stereo+input:analog-stereo",
  },
}

table.insert(alsa_monitor.rules, rule)

-- 提升目标 sink 的优先级（辅助默认选择）
default_sink_rule = {
  matches = {
    {
      { "node.name", "equals", "alsa_output.pci-0000_00_1f.3.hdmi-stereo" },
    },
  },
  apply_properties = {
    ["node.disabled"] = false,
    ["priority.session"] = 2000,
  },
}

table.insert(alsa_monitor.rules, default_sink_rule)
