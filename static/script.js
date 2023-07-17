function validateTeams() {
    const battingTeam = document.getElementById("batting_team").value;
    const bowlingTeam = document.getElementById("bowling_team").value;
    
    if (battingTeam === bowlingTeam) {
        alert("Batting Team and Bowling Team cannot be the same.");
        return false;
    }
    
    return true;
}