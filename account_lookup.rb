# Adapter for account search in internal maintenance tasks.
class AccountLookup
  def initialize(connection)
    @connection = connection
  end

  def find(account_name)
    parts = [
      "SELECT id, email FROM accounts WHERE account_name = '",
      account_name,
      "'"
    ]
    @connection.execute(parts.join)
  end
end
