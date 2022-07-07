function getCurrentTime()
    return os.date("%H:%M:%S")
end

function AlertAllPlayersOfOutage(status, description)
    TriggerClientEvent('chat:addMessage', -1, {
        template = '<div style="font-size: 15px; padding: 0.5vw; margin: 0.5vw; background-color: rgba(255, 0, 0, 0.1); border-radius: 11px;"><i class="fas fa-globe"></i> {0}<br></div>',
          args = { "^1[CFX.re API] - ^7"..status.." [:] "..description }
    })
end





function CheckStatus()
    local Status_Description = ""
    local Status_Issue = ""
    local isDown = false
    PerformHttpRequest("https://status.cfx.re/api/v2/status.json", function(err, text, headers)
        convertJson = json.decode(text)
        Status_Description = convertJson['status']['description']
        Status_Issue = convertJson['status']['indicator']
        if Status_Description ~= "All Systems Operational" then 
            print("====== OUTAGE DETECTED ======")
            print("Time: " ..getCurrentTime())
            print("Found Issue: " .. Status_Issue)
            print("Status: " .. Status_Description)
            isDown = true 
        end 
    end)
    Citizen.Wait(1000)
    return isDown, Status_Description, Status_Issue
end




Citizen.CreateThread(function()
    Result,Description,Issue = CheckStatus()
    if Result == true then
        AlertAllPlayersOfOutage(Description, Issue)
    end
    while true do 
        Citizen.Wait(60000)
        Result,Description,Issue = CheckStatus()
        if Result == true then
            AlertAllPlayersOfOutage(Description, Issue)
        end
    end
end)
