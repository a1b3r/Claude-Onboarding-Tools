# FAQ — Connectors & MCP

> 📖 Pairs with [Module 06](../guide/index.html#m6).

## "Authorization fails / the connector won't connect"
(1) Pop-up blockers often eat the sign-in window — allow pop-ups for claude.ai and
retry. (2) If your account is through a school/employer, the organization may block
third-party app authorizations — that's an admin setting, not a bug. (3) Try
disconnecting fully and reconnecting fresh.

## "Connected, but Claude says it can't access my data"
Scopes matter: you may have granted read access to one thing and be asking about
another (e.g., calendar connected, but you asked about email). Check what
permissions the connector was granted in settings, and confirm the connector is
enabled for *this conversation* — connectors can be toggled per chat.

## "It worked last week, fails now"
Authorizations expire and get revoked (password changes often revoke them).
Reconnect. Also check the service itself isn't down.

## "Claude did something unexpected with a connector"
Stop and review what happened in the conversation — every action Claude takes is
visible there. Going forward: approve actions individually rather than broadly, and
be extra careful when Claude is reading untrusted content (web pages, forwarded
emails) while connectors are live — that's the prompt-injection scenario from
Module 06. You can disconnect any connector instantly in settings.

## "Is connecting X safe?"
The questions to ask: Do I trust the connector's publisher? Does it request the
minimum scopes for what I need? Would I be comfortable with this access being used
in a conversation where Claude also reads random web content? For community MCP
servers (beyond the official directory), the bar is higher — treat them like
installing software, because that's what they are.

## Escalate
https://support.claude.com · MCP standard docs: https://modelcontextprotocol.io
